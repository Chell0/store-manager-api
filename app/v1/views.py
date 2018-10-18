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
        if SALES == []:
            return {"message": "Sorry you have not added any sale records"}, 200
        elif SALES:
            return {'SALES': SALES}

    @classmethod
    def post(cls):
        """Create a sale order."""
        if not request.json:
            return 400

        sale_order = {
            'id': request.json['id'],
            'name': request.json['name'],
            'quantity': request.json['quantity'],
            'price': request.json['price']
        }
        SALES.append(sale_order)
        return {'SALES': SALES}, 201


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
        if PRODUCTS == []:
            return {"message": "Sorry you have not added any products yet"}
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
