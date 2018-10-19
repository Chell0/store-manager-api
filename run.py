"""Global imports."""
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


# local imports
from app.v1.views import OneProduct, ProductList, SaleList, SaleRecord
from app.v1.auth.conf import authentify, identify
from app.v1.auth.user import User

APP = Flask(__name__)  # This will create a Flask wsgi application
API = Api(APP)  # This will create a Flask-RESTful API

jwt = JWT(APP, authentify, identify)

# This will process a GET all and POST request
API.add_resource(SaleList, '/v1/sales')
# This will process a GET by Id request
API.add_resource(SaleRecord, '/v1/sales/<int:id>')
# This will process a GET all and POST request
API.add_resource(ProductList, '/v1/products')
# This will process a GET by Id request
API.add_resource(OneProduct, '/v1/products/<int:id>')

# This will process the authentication request
API.add_resource(User, '/v1/auth')

if __name__ == '__main__':  # This will start a development server
    APP.run(debug=True)
