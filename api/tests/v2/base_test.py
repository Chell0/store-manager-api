"""Importing a test library."""
import unittest

from api import app_create


class BaseTest(unittest.TestCase):
    """Base test class."""

    def setUp(self):
        """This is our set up."""
        self.app = app_create("testing")
        self.client = self.app.test_client()
        self.category = {'name': 'Electonics'}
        self.user = {
            'name': 'machel',
            'email': 'machel@gmail.com',
            'password': 'sadmin'
        }
        self.product = {
            'name': 'Laptop',
            'stock': 'available',
            'price': 50000
        }

        with self.app.app_context():
            # create all tables
            db.create_all()

    def tearDown(self):
        """Tear down."""        
        with self.app.app_context():
            # let's drop all the tables
            db.session.remove()
            db.drop_all()

if __name__ == "__main__":
    unittest.main()
