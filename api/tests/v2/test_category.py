import unittest
import json

# Local imports
from api.tests.v2.base_test import BaseTest


class TestCategories(BaseTest):
    """Test categories class."""

    def test_category_creation(self):
        """Test creating a category (POST request)."""
        response = self.client.post(
            '/v2/categories',
            data=json.dumps({
                'name': "Electronics"
            }),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)

    def test_get_all_categories(self):
        """Test fetching all categories (GET request)."""
        response = self.client.post(
            '/v2/categories',
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)

    def test_get_category_by_name(self):
        """Test fetching a category by name (GET request)."""
        self.client.post(
            '/v2/categories',
            data=json.dumps({
                'name': "Electronics"
            }),
            content_type="application/json"
        )
        response = self.client.get(
            '/v2/categories/{name}',
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
