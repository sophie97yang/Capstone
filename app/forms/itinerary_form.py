from flask_wtf import FlaskForm
from wtforms import DateField,BooleanField,FloatField,IntegerField,StringField
from wtforms.validators import DataRequired
# from datetime import datetime


class ItineraryForm(FlaskForm):
    booking_id = IntegerField('booking_id')
    booking_date=DateField("Booking Date")
    booking_startdate=DateField("Booking Start Date")
    booking_enddate=DateField("Booking End Date")
    booking_time = StringField('Booking Time')
    price = FloatField("Price",validators=[DataRequired()])
    expensed = BooleanField('Expensed')
