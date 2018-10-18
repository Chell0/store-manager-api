# Here we have all the endpoints
from flask import Flask, jsonify, request
from flask_restful import Resource

sales = []


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
