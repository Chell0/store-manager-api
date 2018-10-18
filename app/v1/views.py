"""Here we have all the endpoints."""
from flask import request

from flask_restful import Resource


SALES = []

PRODUCTS = []


# Get all and POST request
class SaleList(Resource):
    """Parent class."""

    @classmethod
    def get(cls):
        """Fetch all sales recorded."""
        return SALES

    @classmethod
    def post(cls):
        """Create a sale order."""
        sale_order = {
            'id': request.json['id'],
            'name': request.json['name'],
            'quantity': request.json['quantity'],
            'price': request.json['price']
        }
        SALES.append(sale_order)
        return {'SALES': SALES}, 200


# GET request by Id
class SaleRecord(Resource):
    """Parent class."""

    @classmethod
    def get(cls, id):
        """Fetch for a single sale order."""
        sales_order = [sale for sale in SALES if sale['id'] == id]
        return {'sale': sales_order[0]}


# Get all and POST request
class ProductList(Resource):
    """Parent class."""

    @classmethod
    def get(cls):
        """Fetch all products."""
        return PRODUCTS

    @classmethod
    def post(cls):
        """Create a product."""
        add_product = {
            'id': request.json['id'],
            'name': request.json['name'],
            'stock': request.json['stock'],
            'price': request.json['price']
        }
        PRODUCTS.append(add_product)
        return {'products': PRODUCTS}, 200


# GET request by Id
class OneProduct(Resource):
    """Parent class."""

    @classmethod
    def get(cls, id):
        """Fetch for a single product."""
        getone = [product for product in PRODUCTS if product['id'] == id]
        return {'product': getone[0]}
