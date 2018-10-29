# Local imports
from api.app.v2.db import StoreDb

from werkzeug.exceptions import NotFound, BadRequest
from werkzeug.security import generate_password_hash, check_password_hash


class Authentication(StoreDb):
    """Authentication class."""

    def __init__(self):
        """Initializing constructor."""
        pass

    def create_user(self, data):
        """Create a user."""
        self.cursor.execute(
            """
            INSERT INTO users (user_name, email, password, is_admin)
            VALUES ('%s', '%s', '%s', '%s') RETURNING user_id
            """
            % (data['user_name'], data['email'], data['password'], data['is_admin'])
        )
        user_id = self.cursor.fetchone()[0]
        self.connection.commit()
        return user_id

    def fetch_email(self, data):
        """Login user."""
        self.cursor.execute("SELECT * FROM users WHERE email='%s'"
            % ('email')
        )
        result = self.cursor.fetchone()[0]
        if not result:
            raise NotFound("Email was not found")
        if result[3] == data['password']:
            return data
        else:
            raise BadRequest("Password does not match")

    def get_user_by_id(self, user_id):
        """Fetch a specific user by id."""
        self.cursor.execute("SELECT * FROM users WHERE user_id='%s'"
            % (user_id)
        )
        result = self.cursor.fetchone()
        return result

    def is_admin_present(self):
        """Check is an admin is present."""
        self.cursor.execute("SELECT * FROM users WHERE is_admin=True"
        )
        result = self.cursor.fetchone()
        return result

    def give_admin_rights(self, email):
        """Give admin rights to a normal user."""
        self.cursor.execute(
            """UPDATE users SET is_admin=True WHERE email='%s'
            """
            % (email)
        )
        self.connection.commit()
        return email
