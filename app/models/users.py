
from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    balance = db.Column(db.Float, default=500)

    trips = db.relationship("TripDetail",back_populates="user")
    expenses_own = db.relationship("Expense",back_populates="payer")
    expenses = db.relationship("ExpenseDetail",back_populates='user')
    updates = db.relationship('ExpenseUpdateDetail',back_populates='user')
    itineraries = db.relationship("Itinerary",back_populates="user")

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        if password == 'OAUTH':
            self.hashed_password = 'OAUTH' # If we look at the password_checker() method, we see that it hashes the user input and compares it
					 ## during login. With this adjustment, even a data breach would NOT expose our Oauth users to
					 ### having their accounts accessed with our default password for Oauth logins, 'OAUTH', as it would never
					 #### hash to that value.
            return
        else:
            self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name':self.last_name,
            'email': self.email,
            'city':self.city,
            'state':self.state,
            'balance':self.balance,
            "trips":[trip.to_dict_trips() for trip in self.trips],
            "expenses_own":[expense.to_dict() for expense in self.expenses_own]
            # "expenses":[expense.to_dict() for expense in self.expenses]
        }


    def to_dict_users(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name':self.last_name,
            'email': self.email,
            'city':self.city,
            'state':self.state,
            'balance':self.balance,
            "expenses_own":[expense.to_dict() for expense in self.expenses_own]
            # "expenses":[expense.to_dict() for expense in self.expenses]
        }
    def to_dict_simple(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name':self.last_name,
            'email': self.email
        }

    # def to_dict_current_user(self,user_id):
    #     return {
    #         'id': self.id,
    #         'first_name': self.first_name,
    #         'last_name':self.last_name,
    #         'email': self.email,
    #         'city':self.city,
    #         'state':self.state,
    #         'balance':self.balance,
    #         "trips":[trip.to_dict_trips(user_id) for trip in self.trips],
    #         "expenses_own":[expense.to_dict() for expense in self.expenses_own]
    #         # "expenses":[expense.to_dict() for expense in self.expenses]
    #     }
