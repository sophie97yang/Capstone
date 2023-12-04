from flask import Blueprint, jsonify,request
from flask_login import login_required,current_user
from ..models import Trip,db,User,Expense,ExpenseDetail

expense_routes = Blueprint('expenses', __name__)

#DELETE AN EXPENSE
@expense_routes.route('/<int:id>/delete',methods=['DELETE'])
@login_required
def delete_expense(id):
    expense = Expense.query.get(id)
    if expense.payer_id!=current_user.id:
        return {'errors':"Forbidden"},403
    if not expense:
        return {'errors': "Expense doesn't exist"}, 404
    trip = Trip.query.get(expense.trip_id)
    db.session.delete(expense)
    db.session.commit()

    #need to update trip at store
    return {'trip': trip.to_dict()}, 200
