"""Thirdparty libraries."""
from flask import Flask
from flask_restful import Api

"""Local imports."""
from instance.config import app_settings
from api.app.v1.views import OneProduct, ProductList, SaleList, SaleRecord


def app_create(config):               
    app = Flask(__name__, instance_path="/instance")
    app.config.from_object(app_settings[config])
    
    api = Api(app)  # This will create a Flask-RESTful API
    # This will process a GET all and POST request
    api.add_resource(SaleList, '/v1/sales')
    # This will process a GET by Id request
    api.add_resource(SaleRecord, '/v1/sales/<int:id>')
    # This will process a GET all and POST request
    api.add_resource(ProductList, '/v1/products')
    # This will process a GET by Id request
    api.add_resource(OneProduct, '/v1/products/<int:id>')

    return app
