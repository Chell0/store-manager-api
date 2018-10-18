# Here we have all the endpoints
from flask import request

from flask_restful import Resource

sales = []
products = []


# Get all and POST request
class SaleList(Resource):

    def get(self):
        """Fetch all sales recorded"""
        return sales

    def post(self):
        """Create a sale order"""
        sale_order = {
            'id': request.json['id'],
            'name': request.json['name'],
            'quantity': request.json['quantity'],
            'price': request.json['price']
        }
        sales.append(sale_order)
        return {'sales': sales}, 200


# GET request by Id
class SaleRecord(Resource):

    def get(self, id):
        """Fetch for a single sale order"""
        sales_order = [sale for sale in sales if sale['id'] == id]
        return {'sale': sales_order[0]}


# Get all and POST request
class ProductList(Resource):

    def get(self):
        """Fetch all products"""
        return products

    def post(self):
        """Create a product"""
        add_product = {
            'id': request.json['id'],
            'name': request.json['name'],
            'stock': request.json['stock'],
            'price': request.json['price']
        }
        products.append(add_product)
        return {'products': products}, 200


# GET request by Id
class OneProduct(Resource):

    def get(self, id):
        """Fetch for a single product"""
        get_one = [product for product in products if product['id'] == id]
        return {'product': get_one[0]}
