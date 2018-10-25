import psycopg2

from  flask_restful import Resource, reqparse

from db import db
from api.app.v2.models.user import UserModel


class UserRegistration(Resource):
    """User registration class."""

    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="Name cannot be blank!"
    )
    parser.add_argument('email',
        type=str,
        required=True,
        help="Email cannot be blank!"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="Password cannot be blank!"        
    )

    def post(self):
        data = UserRegistration.parser.parse_args()

        connection = psycopg2.connect(db)
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message": "User was created successfully."}, 201



