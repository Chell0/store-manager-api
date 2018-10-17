# Here we have all the endpoints
from flask_restful import Resource

sales = {}

class SaleList(Resource):
    def get(self):
        """Fetch all sales recorded"""
        return {'sales': sales}
