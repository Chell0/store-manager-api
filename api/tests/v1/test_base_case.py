"""Importing a test library."""
import unittest

from api import app_create

class BaseTest(unittest.TestCase):
    """Base test class."""
    
    def setUp(self):
        """This is our set up."""
        self.app = app_create("testing")
        self.client = self.app.test_client()

        