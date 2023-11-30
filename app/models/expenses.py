from .db import db, environment, SCHEMA, add_prefix_for_prod

class Expense(db.Model):
    __tablename__ = "expenses"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    payer_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    trip_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("trips.id")))
    name = db.Column(db.String(40), nullable=False)
    expense_date=db.Column(db.Date, nullable=False)
    image = db.Column(db.String(255))
    split_type=db.Column(db.String(50),default='Equal')
    split_type_info=db.Column(db.String(100))
    category=db.Column(db.String(50),default='General')
    total = db.Column(db.Float,nullable=False)

    payer = db.relationship('User',back_populates='expenses_own')
    trip = db.relationship('Trip',back_populates='expenses')
    users = db.relationship('ExpenseDetail',back_populates='expense')


    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "expense_date":self.expense_date,
            "image":self.image,
            "split_type":self.split_type,
            "category":self.category,
            "total":self.total,
            "payer":self.payer_id,
            "trip":self.trip_id
        }
