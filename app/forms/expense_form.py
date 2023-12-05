from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,  FileField, DateField,DecimalField
from wtforms.validators import DataRequired,Length,NumberRange
from flask_wtf.file import FileField, FileAllowed
from ..api.AWS_helpers import ALLOWED_EXTENSIONS
# from datetime import datetime


class ExpenseForm(FlaskForm):
    name = StringField("Trip Name", validators=[DataRequired(), Length(max=40)])
    expense_date=DateField("Expense Date",validators=[DataRequired()])
    image = FileField("Trip Image", validators=[FileAllowed(list(ALLOWED_EXTENSIONS))])
    split_type = SelectField("Split Type", validators=[DataRequired()], choices=[('Equal', 'Equal'), ('Percentages', 'Percentages'), ('Exact', 'Exact')])
    split_type_info=StringField("Split Type Info")
    category=SelectField("Category",validators=[DataRequired()], choices=[('General', 'General'), ('Food and Drink', 'Food and Drink'), ('Transportation', 'Transportation'),('Entertainment', 'Entertainment')])
    total = DecimalField("Total", validators=[DataRequired(), NumberRange(min=1)], places=2)
    users_id = StringField("Users Involved",validators=[DataRequired()])
