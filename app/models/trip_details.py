from .db import db, environment, SCHEMA, add_prefix_for_prod

class TripDetail(db.Model):
    __tablename__= "trip_details"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    trip_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("trips.id")))
    settled = db.Column(db.Boolean,default=False)
    creator = db.Column(db.Boolean,default=False)

    db.UniqueConstraint('user_id','trip_id',name="uix3")
    user = db.relationship("User", back_populates="trips")
    trip = db.relationship("Trip",order_by='Trip.start_date',back_populates="users")

    def to_dict_trips(self):
        return {
            'id': self.id,
            "user_id":self.user_id,
            'trip':self.trip.to_dict(),
            "settled":self.settled,
            "creator":self.creator
        }
    def to_dict_users(self):
        return {
            'id': self.id,
            "user":self.user.to_dict_users(),
            'trip_id':self.trip_id,
            "settled":self.settled,
            "creator":self.creator
        }
    def to_dict(self):
        return {
            'id':self.id,
            "user_id":self.user_id,
            'trip_id':self.trip_id,
            "settled":self.settled,
            "creator":self.creator
        }
