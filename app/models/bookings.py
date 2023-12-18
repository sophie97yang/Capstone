from .db import db, environment, SCHEMA, add_prefix_for_prod


class Booking(db.Model):
    __tablename__= "bookings"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    category = db.Column(db.String(50),nullable=False)
    city = db.Column(db.String(50),nullable=False)
    state= db.Column(db.String(50),nullable=False)
    lat = db.Column(db.Float,nullable=False)
    lng = db.Column(db.Float,nullable=False)
    description =db.Column(db.String(500),nullable=False)
    rating = db.Column(db.Float,nullable=False)
    contact_info=db.Column(db.String(50),nullable=False)
    website = db.Column(db.String(50))
    features = db.Column(db.String(500))
    price= db.Column(db.Float)
    opening_hour = db.Column(db.String(50))
    closing_hour = db.Column(db.String(50))

    image1 = db.Column(db.String(255),nullable=False)
    image2 = db.Column(db.String(255),nullable=False)
    image3 = db.Column(db.String(255),nullable=False)

    trips = db.relationship('Itinerary',back_populates='booking')

    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'category':self.category,
            'city':self.city,
            'state':self.state,
            "price":self.price,
            "description":self.description,
            "rating":self.rating,
            "contact_info":self.contact_info,
            "website":self.website,
            "features":self.features,
            "opening_hour":self.opening_hour,
            "closing_hour":self.closing_hour,
            "image1":self.image1,
            "image2":self.image2,
            "image3":self.image3
        }
