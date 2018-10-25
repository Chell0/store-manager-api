from .db import db

# Sales  Model
class SalesModel(db.Model):
    """This class represents the sales model."""

    __table__ = 'sales'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    quantity = db.Column(db.Integer(80))
    price = db.Column(db.Integer(80))

    def __init__(self, name, quantity, price):
        """initialize the above."""
        self.name = name
        self.quantity = quantity
        self.price = price

    # save sales to db
    def save(self):
        db.session.add(self)
        db.session.commit()

    # get all sales from the db
    @staticmethod
    def get_all_sales():
        return SalesModel.query.all()

    # get a sale order from the db
    @staticmethod
    def get_a_sale_order():
        return SalesModel.query.get(id)
