from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,  FileField, DateField,BooleanField
from wtforms.validators import DataRequired,Length
from flask_wtf.file import FileField, FileAllowed
from ..api.AWS_helpers import ALLOWED_EXTENSIONS
# from datetime import datetime


class TripForm(FlaskForm):
    name = StringField("Trip Name", validators=[DataRequired(), Length(max=40)])
    description = TextAreaField("Description", validators=[Length(max=500)])
    city = StringField("City", validators=[DataRequired(), Length(max=30)])
    state= StringField("State", validators=[DataRequired(), Length(max=30)])
    start_date=DateField("Start Date",validators=[DataRequired()])
    end_date=DateField('End Date',validators=[DataRequired()])
    image = FileField("Trip Image", validators=[FileAllowed(list(ALLOWED_EXTENSIONS))])
    simplify = BooleanField('Simplify Debts')
