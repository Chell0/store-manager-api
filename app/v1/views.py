"""Here we have all the endpoints."""
from flask import request
from flask_restful import Resource
from flask_jwt import jwt_required


SALES = []
PRODUCTS = []


# Get all and POST request
class SaleList(Resource):
    """Parent class."""

    @jwt_required()
    @classmethod
    def get(cls):
        """Fetch all sales recorded."""
        if SALES == []:
            return {"message": "Sorry you have not added any sale records"}
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
        gso = next(filter(lambda x: x['id'] == id, SALES), "Add a sale order")
        return {'gso': gso}, 200 if gso is not "Add a sale order" else 404


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
        gbi = next(filter(lambda x: x['id'] == id, PRODUCTS), "Add a product")
        return {'gbi': gbi}, 200 if gbi is not "Add a product" else 404
