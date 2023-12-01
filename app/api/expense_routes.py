from flask import Blueprint, jsonify,request
from flask_login import login_required,current_user
from ..models import Trip,db,User,Expense,ExpenseDetail

expense_routes = Blueprint('expenses', __name__)
