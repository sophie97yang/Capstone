from .db import db, environment, SCHEMA, add_prefix_for_prod

class ExpenseDetail(db.Model):
    __tablename__= "expense_details"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    expense_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("expenses.id")))
    price = db.Column(db.Float,nullable=False)

    db.UniqueConstraint('user_id','expense_id',name="uix1")
    user = db.relationship("User", back_populates="expenses")
    expense = db.relationship("Expense", back_populates="users")

    def to_dict(self):
        return {
            'id': self.id,
            'price': self.price,
            "user":self.user.to_dict(),
            "expense":self.expense.to_dict()
        }
