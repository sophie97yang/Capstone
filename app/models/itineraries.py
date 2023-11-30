from .db import db, environment, SCHEMA, add_prefix_for_prod

class Itinerary(db.Model):
    __tablename__= "itineraries"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("trips.id")))
    booking_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("bookings.id")))
    booking_date = db.Column(db.Date)
    expensed = db.Column(db.Boolean,default=False)

    db.UniqueConstraint('user_id','booking_id',name="uix2")
    trip = db.relationship("Trip", back_populates="bookings")
    booking = db.relationship("Booking", back_populates="trips")

    def to_dict(self):
        return {
            'id': self.id,
            'booking_date': self.booking_date,
            'expensed':self.expensed,
            "trip":self.trip.to_dict(),
            "booking":self.booking.to_dict()
        }
