from .db import db, environment, SCHEMA, add_prefix_for_prod


class Booking(db.Model):
    __tablename__= "bookings"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    category = db.Column(db.String(50),nullable=False)
    city = db.Column(db.String(50),nullable=False)
    state= db.Column(db.String(50),nullable=False)

    trips = db.relationship('Itinerary',back_populates='booking')

    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'category':self.category,
            'city':self.city,
            'state':self.state,
            'trips_itinerary':[trip.to_dict() for trip in self.trips]
        }
