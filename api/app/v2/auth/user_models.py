# Local imports
# from api.app.v2.db import StoreDb
import os
import psycopg2

from werkzeug.exceptions import NotFound, BadRequest
from werkzeug.security import generate_password_hash, check_password_hash


class Authentication():
    """Authentication class."""

    def __init__(self):
        """Initializing constructor."""
        self.connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        self.cursor = self.connection.cursor()

    def create_user(self, data):
        """Create a user."""
        connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()

        try:
            cursor.execute(
            """
            INSERT INTO users (user_name, email, password)
            VALUES ('%s', '%s', '%s');
            """
            % (data[0], data[1], data[2])
        )
            connection.commit()

        except:
            return "Failed"
        return {'message': "You have successfully registered"}

    def fetch_email(self, data):
        """Login user."""
        connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email= '{}'".format(data))
        connection.commit()
        result = cursor.fetchall()

        if not result:
            return ({"status": "Email was not found"}), 404
        return result
        if result[2] == data['password']:
            return result[0]
        else:
            raise BadRequest("Password does not match")

    def get_user_by_id(self, user_id):
        """Fetch a specific user by id."""
        self.connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        self.cursor = connection.cursor()
        self.cursor.execute("SELECT * FROM users WHERE user_id='%s'"
            % (user_id)
        )
        result = self.cursor.fetchone()
        return result

    def is_admin_present(self):
        """Check is an admin is present."""
        self.connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        self.cursor = connection.cursor()

        self.cursor.execute("SELECT * FROM users WHERE is_admin=True"
        )
        result = self.cursor.fetchone()
        return result

    def give_admin_rights(self, email):
        """Give admin rights to a normal user."""
        self.connection = psycopg2.connect(os.getenv("DATABASE_URL"))
        self.cursor = connection.cursor()
        self.cursor.execute(
            """
            UPDATE users SET is_admin=True WHERE email='%s'
            """
            % (email)
        )
        self.connection.commit()
        return email


