from .db import db, environment, SCHEMA, add_prefix_for_prod

class Expense(db.Model):
    __tablename__ = "expenses"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    payer_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    trip_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("trips.id")))
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(500))
    expense_date=db.Column(db.Date, nullable=False)
    image = db.Column(db.String(255))
    split_type=db.Column(db.String(50),default='Equal')
    category=db.Column(db.String(50),default='General')
    total = db.Column(db.Float,nullable=False)
    settled= db.Column(db.Boolean,default=False)

    payer = db.relationship('User',back_populates='expenses_own')
    trip = db.relationship('Trip',back_populates='expenses')
    users = db.relationship('ExpenseDetail',back_populates='expense')


    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "description":self.description,
            "expense_date":self.expense_date,
            "image":self.image,
            "split_type":self.split_type,
            "category":self.category,
            "total":self.total,
            "settled":self.settled,
            "payer":self.payer.to_dict(),
            "trip":self.trip.to_dict(),
            "users":[user.to_dict() for user in self.users]
        }
