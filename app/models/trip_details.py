from .db import db, environment, SCHEMA, add_prefix_for_prod

class TripDetail(db.Model):
    __tablename__= "trip_details"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    trip_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("trips.id")))
    settled = db.Column(db.Float,default=False)

    db.UniqueConstraint('user_id','trip_id',name="uix3")
    user = db.relationship("User", back_populates="trips")
    trip = db.relationship("Trip", back_populates="users")

    def to_dict(self):
        return {
            'id': self.id,
            'user':self.user.to_dict(),
            'trip':self.trip.to_dict(),
            "settled":self.settled
        }
