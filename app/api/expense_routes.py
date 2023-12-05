from flask import Blueprint, jsonify,request
from flask_login import login_required,current_user
from ..models import Trip,db,User,Expense,ExpenseDetail,BetweenUserExpense

expense_routes = Blueprint('expenses', __name__)

#DELETE AN EXPENSE
@expense_routes.route('/<int:id>/delete',methods=['DELETE'])
@login_required
def delete_expense(id):
    expense = Expense.query.get(id)
    #ONLY THOSE WHO HAVE CREATED THE EXPENSE CAN DELETE IT
    if expense.payer_id!=current_user.id:
        return {'errors':"Forbidden"},403
    if not expense:
        return {'errors': "Expense doesn't exist"}, 404

    trip = Trip.query.get(expense.trip_id)
    #UPDATE THE EXPENSE RELATIONSHIP BETWEEN USERS INVOLVED ACCORDINGLY

    # #check if there is already an existing expense relationship between two users in trip - THERE SHOULD ALWAYS BE A RELATIONSHIP
    # relationship_one = BetweenUserExpense.query.filter_by(user_one_id=current_user.id,user_two_id=,trip_id=trip.id).first()
    # relationship_two= BetweenUserExpense.query.filter_by(user_one_id=,user_two_id=current_user.id,trip_id=trip.id).first()
    relationship_one = [relationship for relationship in trip.between_user_expenses if relationship.user_one_id==current_user.id]
    relationship_two = [relationship for relationship in trip.between_user_expenses if relationship.user_two_id==current_user.id]
    for relationship in relationship_one:
            #user_one=payer,user_two=user involved in expense
            #user_one now is not owed the cost of the expense for the other user
            #query expense detail to get that price
            expense_detail = ExpenseDetail.query.filter_by(user_id=relationship.user_two_id,expense_id=id).first()
            relationship.owed-=expense_detail.price
    for relationship in relationship_two:
            #user_one=user involved in expense, user_two=payer
            #user_one now does not owe the cost of the expense for that user
            expense_detail = ExpenseDetail.query.filter_by(user_id=relationship.user_two_id,expense_id=id).first()
            relationship.owes-=expense_detail.price

    trip = Trip.query.get(expense.trip_id)
    db.session.delete(expense)
    db.session.commit()

    #need to update trip at store
    return {'trip': trip.to_dict()}, 200
