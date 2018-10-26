# Local imports
from api.app.v2.db import StoreDb

from werkzeug.exceptions import NotFound, BadRequest


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

    def login(self, data):
        """Login user."""
        self.cursor.execute(
            """
            SELECT * FROM users WHERE email='%s'
            """
            % (data['email'])
        )
        result = self.cursor.fetchone()[0]
        if not result:
            raise NotFound("Email not found")
        if result[3] == data['password']:
            return data
        else:
            raise BadRequest("password do not match")
