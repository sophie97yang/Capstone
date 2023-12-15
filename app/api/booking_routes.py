from flask import Blueprint, jsonify,request
from flask_login import login_required,current_user
from ..models import Booking
from datetime import date

booking_routes = Blueprint('bookings',__name__)

#get all bookings
@booking_routes.route('/all',methods=['GET'])
def get_bookings():
    bookings = Booking.query.all()
    return {"bookings":[booking.to_dict() for booking in bookings]}

#add a booking to a trip's itinerary
@booking_routes.route('/:id/add',methods=['POST'])
def add_booking():
    pass
