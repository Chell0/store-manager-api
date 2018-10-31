"""Importing a test library."""
import unittest

import os

importjson

from api import app_create

from db import db


class BaseTest(unittest.TestCase):
    """Base test class."""

    def setUp(self):
        """This is our set up."""
        self.app = app_create("testing")
        self.client = self.app.test_client
