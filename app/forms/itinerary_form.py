from flask_wtf import FlaskForm
from wtforms import DateField,TimeField,BooleanField,FloatField
from wtforms.validators import DataRequired
# from datetime import datetime


class ItineraryForm(FlaskForm):
    booking_date=DateField("Booking Date")
    booking_startdate=DateField("Booking Start Date")
    booking_enddate=DateField("Booking End Date")
    booking_time = TimeField('Booking Time')
    price = FloatField("Price",validators=[DataRequired()])
    expensed = BooleanField('Expensed')
