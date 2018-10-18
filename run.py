"""Global imports."""
from flask import Flask
from flask_restful import Api

# local imports
from app.v1.views import OneProduct, ProductList, SaleList, SaleRecord


APP = Flask(__name__)  # This will create a Flask wsgi application
API = Api(APP)  # This will create a Flask-RESTful API

# This will process a GET all and POST request
API.add_resource(SaleList, '/v1/sales')
# This will process a GET by Id request
API.add_resource(SaleRecord, '/v1/sales/<int:id>')
# This will process a GET all and POST request
API.add_resource(ProductList, '/v1/products')
# This will process a GET by Id request
API.add_resource(OneProduct, '/v1/products/<int:id>')

if __name__ == '__main__':  # This will start a development server
    APP.run(debug=True)
