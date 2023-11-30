from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,  FileField, DateField,DecimalField
from wtforms.validators import DataRequired,Length,NumberRange
from flask_wtf.file import FileField, FileAllowed
from ..api.AWS_helpers import ALLOWED_EXTENSIONS
# from datetime import datetime


class ExpenseForm(FlaskForm):
    name = StringField("Trip Name", validators=[DataRequired(), Length(max=40)])
    expense_date=DateField("Start Date",validators=[DataRequired()])
    image = FileField("Trip Image", validators=[FileAllowed(list(ALLOWED_EXTENSIONS))])
    split_type = SelectField("Split Type", validators=[DataRequired()], choices=[('Equal', 'Equal'), ('Percentages', 'Percentages'), ('Exact', 'Exact')])
    price = DecimalField("Price", validators=[DataRequired(), NumberRange(min=1)], places=2)
