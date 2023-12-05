from .db import db, environment, SCHEMA, add_prefix_for_prod

class Trip(db.Model):
    __tablename__ = "trips"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(500))
    city = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(30), nullable=False)
    start_date=db.Column(db.Date, nullable=False)
    end_date=db.Column(db.Date, nullable=False)
    image = db.Column(db.String(255))
    #bonus feature
    simplify = db.Column(db.Boolean, default=False)

    expenses = db.relationship('Expense',back_populates='trip',cascade="all, delete")
    users = db.relationship('TripDetail',back_populates='trip',cascade="all, delete",order_by="TripDetail.user_id")
    bookings = db.relationship('Itinerary',back_populates='trip')
    between_user_expenses = db.relationship('BetweenUserExpense',back_populates='trip',cascade="all,delete")

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "description":self.description,
            "location":(self.city,self.state),
            "start_date":self.start_date,
            "end_date":self.end_date,
            "image":self.image,
            "expenses":[expense.to_dict() for expense in self.expenses],
            "users":[user.to_dict_simple() for user in self.users],
            "bookings_itinerary":[booking.to_dict() for booking in self.bookings],
            "between_user_expenses":[relationship.to_dict() for relationship in self.between_user_expenses]
        }

    def to_dict_users(self):
        return {
            "id":self.id,
            "name":self.name,
            "description":self.description,
            "location":(self.city,self.state),
            "start_date":self.start_date,
            "end_date":self.end_date,
            "image":self.image,
            "expenses":[expense.to_dict() for expense in self.expenses],
            "users":[user.to_dict_users() for user in self.users],
            "bookings_itinerary":[booking.to_dict() for booking in self.bookings]
        }

    def to_dict_simple(self):
        return {
            "id":self.id,
            "name":self.name,
            "description":self.description,
            "location":(self.city,self.state),
            "start_date":self.start_date,
            "end_date":self.end_date,
            "image":self.image,
            "expenses":[expense.to_dict() for expense in self.expenses],
            "users":[user.to_dict_simple() for user in self.users],
            "bookings_itinerary":[booking.to_dict() for booking in self.bookings]
        }

    # def to_dict_current_user(self,user_id):
    #     return {
    #         "id":self.id,
    #         "name":self.name,
    #         "description":self.description,
    #         "location":(self.city,self.state),
    #         "start_date":self.start_date,
    #         "end_date":self.end_date,
    #         "image":self.image,
    #         "expenses":[expense.to_dict_current_user(user_id) for expense in self.expenses],
    #         "users":[user.to_dict_users() for user in self.users],
    #         "bookings_itinerary":[booking.to_dict() for booking in self.bookings]
    #     }
