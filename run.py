# local imports
from app.v1.views import ProductList, SaleList, SaleRecord

from flask import Flask

from flask_restful import Api, Resource


app = Flask(__name__)  # This will create a Flask wsgi application

api = Api(app)  # This will create a Flask-RESTful API

# This will process a GET all and POST request
api.add_resource(SaleList, '/v1/sales')
# This will process a GET by Id request
api.add_resource(SaleRecord, '/v1/sales/<int:id>')
# This will process a GET all and POST request
api.add_resource(ProductList, '/v1/products')


if __name__ == '__main__':  # This will start a development server
    app.run(debug=True)