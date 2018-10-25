import unittest
import os
import json

# Local imports
from api.tests.v2.base_test import BaseTest
from db import db


class TestUsers(BaseTest):
    """Test users class."""

    def test_create_user(self):
        """Testing how to create a user."""
        response = self.client.post(
            '/v2/auth/signup',
            data=json.dumps({
                'name': 'machel',
                'email': 'machel@gmail.com',
                'password': 'sadmin'
            }),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)

    def test_user_login(self):
        """Test user login."""
        response = self.client.post(
            '/v2/auth/signup',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(self.user)
        )
        self.assertEqual(response.status_code, 201)
        response = self.client.post(
            '/v2/auth/login',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(self.user)
        )
        data = json.loads(response.data)
        self.assertTrue(data.get('secret'))
        self.assertEqual(response.status_code, 200)
