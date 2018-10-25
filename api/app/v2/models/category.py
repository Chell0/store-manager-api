from api.app.v2.db import db

# Category Model
class CategoryModel(db.Model):
    """This class represents the category model."""

    __table__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name

    # save to db
    def save(self):
        db.session.add(self)
        db.session.commit()

    # get all categories
    @staticmethod
    def get_all_categories():
        return CategoryModel.query.all()

    # get a single category
    @staticmethod
    def get_category_by_name(name):
        return CategoryModel.query.get(name)
