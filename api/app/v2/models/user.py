from api.app.v2.db import db

# Users Model
class UserModel(db.Model):
    """This class represents the users model."""

    __table__ = 'users'

    # These are compulsory fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True,  nullable=False)
    password = db.Column(db.String(150), nullable=True)

    def __init__(self, name, email, password):
        """initialize with above."""
        self.name = 'name'
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
    def get_a_single_user():
        return UserModel.query.get(id)
