from .db import db, environment, SCHEMA, add_prefix_for_prod

class Itinerary(db.Model):
    __tablename__= "itineraries"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("trips.id")))
    booking_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("bookings.id")))
    user_id = db.Column(db.Integer,db.ForeignKey(add_prefix_for_prod("users.id")))
    booking_date = db.Column(db.Date)
    booking_startdate = db.Column(db.Date)
    booking_enddate = db.Column(db.Date)
    booking_time = db.Column(db.String(15))
    expensed = db.Column(db.Boolean,default=False)
    total = db.Column(db.Float)

    db.UniqueConstraint('trip_id','booking_id',name="uix2")
    trip = db.relationship("Trip", back_populates="bookings")
    booking = db.relationship("Booking", back_populates="trips")
    user = db.relationship("User",back_populates="itineraries")

    def to_dict(self):
        return {
            'id': self.id,
            'booking_date': self.booking_date,
            'expensed':self.expensed,
            "booking_startdate":self.booking_startdate,
            "booking_enddate":self.booking_enddate,
            "booking_time":self.booking_time,
            "total":self.total,
            "booking":self.booking.to_dict(),
            "creator":self.user.to_dict_simple()
        }
