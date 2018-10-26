from flask_restful import Resource, reqparse

# local imports
from api.app.v2.auth.user_models import Authentication
usr = Authentication()


class Login(Resource):
    """Login class."""

    def add_user(self):
        usr.create_user()
