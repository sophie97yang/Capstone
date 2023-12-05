from .db import db, environment, SCHEMA, add_prefix_for_prod

class ExpenseUpdateDetail(db.Model):
    __tablename__= "expense_update_details"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    expense_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("expenses.id")))
    update_date=db.Column(db.Date, nullable=False)
    update_type=db.Column(db.String(50))
    update_info=db.Column(db.String(100))

    expense = db.relationship("Expense", back_populates="updates")
    user = db.relationship("User", back_populates="updates")

    def to_dict(self):
        return {
            'id': self.id,
            'update_date': self.update_date,
            "update_type":self.update_type,
            "update_info":self.update_info,
            "user":self.user.to_dict_simple()
        }
