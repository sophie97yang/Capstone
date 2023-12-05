from .db import db, environment, SCHEMA, add_prefix_for_prod

class BetweenUserExpense(db.Model):
    __tablename__= "between_user_expenses"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_one_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    user_two_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    trip_id = db.Column(db.Integer,db.ForeignKey(add_prefix_for_prod("trips.id")))
    #user one -> user two
    owed = db.Column(db.Float,default=0.00)
    owes = db.Column(db.Float,default=0.00)

    user_one = db.relationship('User', foreign_keys=[user_one_id])
    user_two = db.relationship('User', foreign_keys=[user_two_id])
    trip = db.relationship('Trip',back_populates='between_user_expenses')
