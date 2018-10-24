import unittest
import os
import json

# Local imports
from api import app_create

class TestUsers(unittest.Testcase):
    """Testing users."""

    def setUp(self):
        """Setup Test."""
        self.app = app_create("testing")
        self.client = self.app.test_client()
        self.user = {
            'name': 'machel',
            'email': 'machel@gmail.com',
            'password': 'sadmin' 
        }

        with self.app.app_context():
            # create all tables
            db-create_all()

    def test_create_user(self):
        """Testing how to create a user."""
        response = self.client().post(
            '/v2/auth/signup',
            data=json.dumps({
                'name': 'machel',
                'email': 'machel@gmail.com',
                'password': 'sadmin'
            }),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)

    def test_user_login(self):
        """Test user login."""
        response = self.client.post(
            '/v2/auth/signup',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(self.user)
        )
        self.assertEqual(response.status_code, 201)
        response = self.client().post(
            '/v2/auth/login',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(self.user)
        )
        data = json.loads(response.data)
        self.assertTrue(data.get('secret'))
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        """Tear down."""
        with self.app.app_context():
            # let's drop all the tables
            db.session.remove()
            db.drop_all()

if __name__ == "__main__":
    unittest.main()
