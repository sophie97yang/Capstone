from flask_wtf import FlaskForm
from wtforms import StringField

class AddUserForm(FlaskForm):
    email_1 = StringField("Email 1")
    email_2 = StringField("Email 1")
    email_3 = StringField("Email 1")
