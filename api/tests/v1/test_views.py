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
