import unittest
import json

# Local imports
from api import app_create
from api.tests.v2.base_test import BaseTest
from db import db


class TestUsers(BaseTest):
    """Test users class."""

    def test_user_registration(self):
        """Test if user registration is working."""
        res = self.client().post('/v2/auth/signup', data=self.user_data)
        # get the results in json format
        result = json.loads(res.data.decode())
        self.assertEqual(result['message'], 'You have been registered successfully.')
        self.assertEqual(res.status_code, 201)

    def test_user_existence(self):
        """Test if user exists to avoid double registration."""
        res = self.client().post('/v2/auth/signup', data=self.user_data)
        self.assertEqual(re.status_code, 201)
        second_res = self.client().post(
            '/v2/auth/signup',
            data=self.user_data)
        self.assertEqual(second_res.status_code, 202)
        # get the results in json format
        result = json.loads(second_res.data.decode())
        self.assertEqual(
            result['message'], "Uh-oh user already exists. Please login."
        )

    def test_user_login(self):
        """Test if registered user can login."""
        res = self.client().post('/v2/auth/signup', data=self.user_data)
        self.assertEqual(res.status_code, 201)
        user_login_res = self.client().post('v2/auth/login', data=self.user_data)

        # get the results in json format
        result = json.loads(user_login_res.data.decode())
        # Test if response contains a success message
        self.assertEqual(result['message'], "You have logged in successfully.")
        self.assertEqual(user.user_login_res.status_code, 200)
        self.assertTrue(result['access_token'])


    def test_not_registered_user_login(self):
        """Test if a non registered user is able to login."""
        # define a dict to represent a non registered user
        does_not_exist = {
            'email': 'doe@ymail.com',
            'password': 'missing'
        }
        # send a POST request
        res = self.client().post('/v2/auth/login', data=does_not_exist)
        # get the result in json
        result = json.loads(res.dat.decode())

        # add a message and an error status code 401(Unauthorized)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(
            result['message'], "Uh-oh, invalid email or password. Please try again")
