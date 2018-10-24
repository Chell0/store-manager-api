from marshmallow import fields, Schema
from db import db

# Users Model
class UserModel(db.Model):
    """This class represents the users model."""

    __table__ = 'users'

    # These are compulsory fields
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(150), nullable=False)
    user_email = db.Column(db.String(150), unique=True,  nullable=False)
    user_password = db.Column(db.String(150), nullable=True)

    def __init__(self, data):
        """initialize with name."""
        self.name = data.get('name')
        self.email = data.get('email')
        self.password = data.get('password')

    # save users to db
    def save(self):
        db.session.add(self)
        db.session.commit()

    # get all users from the db
    @staticmethod
    def get_all():
        return UserModel.query.all()

    # get a single user from the db
    @staticmethod
    def get_a_single_user():
        return UserModel.query.get(id)

    def __repr__(self):
        return "<name {}>".format(self.name)
