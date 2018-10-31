import unittest
import json

# Local imports
from store-manager-api.api.v2.base_test import BaseTest


class StoreTestCase(BaseTest):
    """This class represents the category test case."""

    def register_a_user(self, email='user1@test.com', password='testing123'):
        """This helper method helps register a test user."""
        user_data = {'email': email, 'password': password}
        return self.client().post('/v2/auth/signup', data=user_data)

    def login_a_user(self, email='user1@test.com', password='testing123'):
        """This helper method helps login a test user."""
        user_data = {'email': email, 'password': password}
        return self.client().post('/v2/auth/login', data=user_data)

    def test_create_category(self):
        """Test if the API can create a category (POST request)."""
        # register a test user, then log them in
        self.register_a_user()
        result = self.login_a_user()
        # obtain the access token
        access_token = json.loads(result.data.decode())['access_token']

        # create a category with a POST request
        response = self.client().post(
            '/v2/categories',
            headers=dict(Authorization="Bearer " + access_token),
            data=self.category)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Electronics', str(response.data))

    def test_get_all_categories(self):
        """Test if API can fetch all categories (GET request)."""
        self.register_a_user()
        result = self.login_a_user()
        # obtain the access token
        access_token = json.loads(result.data.decode())['access_token']

        # create a category with a POST request
        response = self.client().post(
            '/v2/categories',
            headers=dict(Authorization="Bearer " + access_token),
            data=self.category)
        self.assertEqual(response.status_code, 201)

        # get all categories
        response = self.client.post(
            '/v2/categories',
            headers=dict(Authorization="Bearer " + access_token)
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('Electronics', str(response.data))

    def test_get_category_by_id(self):
        """Test if API can fetch a category by it's id (GET request)."""
        self.register_a_user()
        result = self.login_a_user()
        access_token = json.loads(result.data.decode())['access_token']

        rv = self.client().post(
            '/v2/categories',
            headers=dict(Authorization="Bearer " + access_token),
            data=self.category            
        )
        # assert that the category is created
        self.assertEqual(rv.status_code, 201)
        # get the response of data in json format
        results = json.loads(rv.data.decode())

        result = self.client().get(
            '/v2/categories/{}'.format(results['id']),
            headers=dict(Authorization="Bearer " + access_token)
        )

        # assert that the category is actually returned given its ID
        self.assertEqual(result.status_code, 200)
        self.assertIn('Electronics', str(result.data))

    def test_category_can_be_modified(self):
        """Test API can edit an existing category (PUT request)."""
        self.register_a_user()
        result = self.login_a_user()
        access_token = json.loads(result.data.decode())['access_token']

        # create a category (POST request)
        rv = self.client().post(
            '/v2/categories',
            headers=dict(Authorization="Bearer " + access_token),
            data={'category_name': 'Electronics'})
        self.assertEqual(rv.status_code, 201)
        # get the response in json format
        results = json.loads(rv.data.decode())

        # edit the created category(PUT request)
        rv = self.client().put(
            '/v2/categories/1',
            headers=dict(Authorization="Bearer " + access_token),
            data={
                "category_name": "Furniture"
            })
        self.assertEqual(rv.status_code, 200)

        # get the modified category to see if it is actually edited.
        results = self.client().get(
            '/v2/categories/{}'.format(results['id']),
            headers=dict(Authorization="Bearer " + access_token))
        self.assertIn('Furniture', str(results.data))

    def test_category_deletion(self):
        """Test if API can delete an existing category (DELETE request)."""
        self.register_a_user()
        result = self.login_a_user()
        access_token = json.loads(result.data.decode())['access_token']

        rv = self.client().post(
            '/v2/categories',
            headers=dict(Authorization="Bearer " + access_token),
            data={'category_name': 'Electronics'})
        self.assertEqual(rv.status_code, 201)
        # get the category in json
        results = json.loads(rv.data.decode_token())

        # delete the category
        res = self.client().delete(
            '/v2/categories/{}'.format(results['id']),
            headers=dict(Authorization="Bearer " + access_token),)
        self.assertEqual(res.status_code, 200)

        # Test to see if category exists, should return a 404
        result = self.client().get(
            '/v2/categories/1',
            headers=dict(Authorization="Bearer " + access_token))
        self.assertEqual(result.status_code, 404)

# Make the tests executable
if __name__ == "__main__":
    unittest.main()
