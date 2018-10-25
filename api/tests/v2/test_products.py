import unittest
import json

# Local imports
from api.tests.v2.base_test import BaseTest


class TestProducts(BaseTest):
    """Test products class."""

    def test_product_creation(self):
        """Test creating a product (POST request)."""
        response = self.client.post(
            '/v2/products',
            data=json.dumps({
                'name': "Laptop",
                'stock': "available",
                'price': 50000
            }),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)

    def test_get_all_products(self):
        """Test fetching all products (GET request)."""
        response = self.client.post(
            '/v2/products',
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)

    def test_get_product_by_name(self):
        """Test fetching a product by name (GET request)."""
        response = self.client.post(
            '/v2/categories',
            data=json.dumps({
                'name': "Laptop",
                'stock': "available",
                'price': 50000
            }),
            content_type="application/json"
        )
        response = self.client.get(
            '/v2/categories/{name}',
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
