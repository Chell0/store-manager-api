from api.app.v2.db import db

# Products Model
class ProductModel(db.Model):
    """This class represents the products model."""

    __table__ = 'products'

    id = db.Column(db.Integer, primary=True)
    name = db.Column(db.String(80))
    stock = db.Column(db.String(80))
    price = db.Column(db.Integer)

    def __init__(self, name, stock, price):
        self.name = name
        self. stock = stock
        self.price = price

    # save products to db
    def save(self):
        db.session.add(self)
        db.session.commit()

    # get all products from the db
    @staticmethod
    def get_all_categories():
        return ProductModel.query.all()

    # get a single product from the db
    @staticmethod
    def get_one_product():
        return ProductModel.query.get(id)
