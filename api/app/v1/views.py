"""Here we have all the endpoints."""
from flask import request
from flask_restful import Resource
# from flask_jwt import jwt_required

sales = []
products = []

# Get all and POST request
class SaleList(Resource):
    """Parent class."""

    # @jwt_required()
    @classmethod
    def get(cls):
        """Fetch all sales recorded."""
        if sales == []:
            return {"message": "Sorry you have not added any sale records"}
        elif sales:
            return {'sales': sales}

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
        sales.append(sale_order)
        return {'sales': sales}, 201


# GET request by Id
class SaleRecord(Resource):
    """Parent class."""

    @classmethod
    def get(cls, id):
        """Fetch for a single sale order."""
        sale_by_id = next(filter(lambda x: x['id'] == id, sales), "Add a sale order")
        return {'sale_by_id': sale_by_id}, 200 if sale_by_id is not "Add a sale order" else 404


# Get all and POST request
class ProductList(Resource):
    """Parent class."""

    @classmethod
    def get(cls):
        """Fetch all products."""
        if products == []:
            return {"message": "Sorry you have not added any products yet"}
        return products

    @classmethod
    def post(cls):
        """Create a product."""
        add_product = {
            'id': request.json['id'],
            'name': request.json['name'],
            'stock': request.json['stock'],
            'price': request.json['price']
        }
        products.append(add_product)
        return {'status':"success", 'products': products}, 201


# GET request by Id
class OneProduct(Resource):
    """Parent class."""

    @classmethod
    def get(cls, id):
        """Fetch for a single product."""
        get_by_id = next(filter(lambda x: x['id'] == id, products), "Add a product")
        return {'get_by_id': get_by_id}, 200 if get_by_id is not "Add a product" else 404
