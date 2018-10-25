
from .db import db

# Users Model
class UserModel(db.Model):
    """This class represents the users model."""

    __table__ = 'users'

    # These are compulsory fields
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True,  nullable=False)
    password = db.Column(db.String(150), nullable=True)

    def __init__(self, username, email, password):
        """initialize with above."""
        self.username = 'username'
        self.email = 'email'
        self.password = 'password'

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
    def get_by_id(id):
        return UserModel.query.filter_by(id=id).first()

    # get a single user by name
    @staticmethod
    def get_by_name(username):
        return UserModel.query.filter_by(username=username).first()
