from flask import Flask
from flask_restful import Resource, Api

# local imports
from app.v1.views import SaleList


app = Flask(__name__) # This will create a Flask wsgi application
api = Api(app) # This will create a Flask-RESTful API

api.add_resource(SaleList, '/v1/sales') # This will process a GET and POST request


if __name__ == '__main__': # This will start a development server
    app.run(debug=True)
