import unittest
import json

# Local imports
from api.tests.v1.test_base_case import BaseTest


class TestFlaskApi(BaseTest):
    """Testing out Flask Api."""

    def test_get_all_sales(self):
        """Test fetching all sales."""
        mac = self.client.get(
            '/v1/sales',
            content_type="application/json"
        )
        self.assertEqual(mac.status_code, 200)

    def test_add_sale_order(self):
        """Test how to create a sale order."""
        mac = self.client.post(
            '/v1/sales',
            data=json.dumps({
                'id': 1,
                'name': "Watch",
                'quantity': 3,
                'price': 45000
            }),
            content_type="application/json"
        )
        self.assertEqual(mac.status_code, 201)

    def test_get_specific_sale_order(self):
        """Test fetching a single sale order."""
        self.client.post(
            '/v1/sales',
            data=json.dumps({
                'id': 1,
                'name': "Watch",
                'quantity': 3,
                'price': 45000
            }),
            content_type="application/json"
        )
        mac = self.client.get(
            '/v1/sales/1',
            content_type="application/json"
        )
        self.assertEqual(mac.status_code, 200)

    def test_get_all_products(self):
        """Test fetching all products."""
        mac = self.client.get(
            '/v1/products',
            content_type="application/json"
        )
        self.assertEqual(mac.status_code, 200)
        
    def test_add_product(self):
        """Test how to create a product."""
        mac = self.client.post(
            '/v1/products',
            data=json.dumps({
                'id': 1,
                'name': "Watch",
                'stock': "available",
                'price': 25000
            }),
            content_type="application/json"
        )
        self.assertEqual(mac.status_code, 201)

    def test_get_a_specific_product(self):
        """Test fetching a single product."""
        self.client.post(
            '/v1/products',
            data=json.dumps({
                'id': 1,
                'name': "Watch",
                'stock': "available",
                'price': 25000
            }),
            content_type="application/json"
        )
        mac = self.client.get(
            '/v1/products/1',
            content_type="application/json"
        )
        self.assertEqual(mac.status_code, 200)
