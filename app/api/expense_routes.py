from flask import Blueprint, jsonify,request
from flask_login import login_required,current_user
from ..models import Trip,db,User,Expense,ExpenseDetail,BetweenUserExpense,Itinerary

expense_routes = Blueprint('expenses', __name__)

#DELETE AN EXPENSE
@expense_routes.route('/<int:id>/delete',methods=['DELETE'])
@login_required
def delete_expense(id):
    expense = Expense.query.get(id)
    itinerary = Itinerary.query.filter(Itinerary.expense_id==id and Itinerary.trip_id==expense.trip_id).first()
    print('ITINERARRRYYYYY',itinerary)
    #ONLY THOSE WHO HAVE CREATED THE EXPENSE CAN DELETE IT
    if expense.payer_id!=current_user.id:
        return {'errors':"Forbidden"},403
    if not expense:
        return {'errors': "Expense doesn't exist"}, 404

    trip = Trip.query.get(expense.trip_id)
    #UPDATE THE EXPENSE RELATIONSHIP BETWEEN USERS INVOLVED ACCORDINGLY
    relationship_one = [relationship for relationship in trip.between_user_expenses if relationship.user_one_id==current_user.id and not(relationship.user_one_id==current_user.id and relationship.user_two_id==current_user.id) and not relationship.owed==0]
    relationship_two = [relationship for relationship in trip.between_user_expenses if relationship.user_two_id==current_user.id and not(relationship.user_one_id==current_user.id and relationship.user_two_id==current_user.id) and not relationship.owes==0]

    for relationship in relationship_one:
            #user_one=payer,user_two=user involved in expense
            #user_one now is not owed the cost of the expense for the other user
            #query expense detail to get that price
            expense_detail = ExpenseDetail.query.filter_by(user_id=relationship.user_two_id,expense_id=id).first()
            if  expense_detail:
                relationship.owed-=expense_detail.price
    for relationship in relationship_two:
            #user_one=user involved in expense, user_two=payer
            #user_one now does not owe the cost of the expense for that user
            expense_detail = ExpenseDetail.query.filter_by(user_id=relationship.user_one_id,expense_id=id).first()
            if expense_detail:
                relationship.owes-=expense_detail.price

    # trip = Trip.query.get(expense.trip_id)
    db.session.delete(expense)
    if itinerary:
        itinerary.expense_id=None
        itinerary.expensed=False
    db.session.commit()

    #need to update trip at store
    return {'trip': trip.to_dict(),'itinerary':itinerary.to_dict()}, 200
