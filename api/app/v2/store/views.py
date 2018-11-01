from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import BadRequest, NotFound, Unauthorized

import re

# local imports
from api.app.v2.store.model import StoreModel as db_model

class StoreProducts(Resource):
	"""Store products class."""

	def __init__(self):
		pass

	@jwt_required
	def post(self):
		"""Add a product to the store."""
		parser = reqparse.RequestParser()
		parser.add_argument('product_name',
			type=str,
			required=True,
			help="Product name cannot be left blank!"
		)
		parser.add_argument('stock_quantity',
			type=int,
			required=True,
			help="Stock status cannot be left blank!"
		)
		parser.add_argument('price',
			type=int,
			required=True,
			help="Price cannot be left blank!"
		)
		parser.add_argument('category_id',
			type=int,
			required=True,
			help="Category name cannot be left blank!"
		)
		args = parser.parse_args()
		product_name = args['product_name']
		category_id = args['category_id']
		data = [product_name, stock_quantity, price, category_id]
		return db_model.add_category(self, data)
		if product_name:
			return {'message': "Error, products already exists"}, 409
		else:
			return {'message': "Product has been added successfuly"}, 201

	def get(self):
		"""Fetch all products."""
		products = db_model.get_all_products()
		if len(products) == 0:
			return {"message": "Sorry, there are no products"}, 200

	def put(self, stock_quantity):
		"""Modify a product."""
		parser = reqparse.RequestParser()
		parse.add_argument('stock_quantity',
			type=int,
			required=True,
			help="Stock cannot be left blank!"
		)
		args = parser.parse_args()
		product = db_model.modify_a_product(id)
		return product


	def delete(self, id):
		"""Delete a product."""
		product = db_model.get_one_product(id)
		product_id = db_model.delete_a_category(id)
		if product:
			return {"messages": "Product was deleted successfully!"}, 204
		else:
			return {"message": "Product was not found"}, 404

class OneStoreProduct(Resource):
	"""One product class."""

	@jwt_required
	def get(self, id):
		"""Fetch a single product by its ID."""
		product_id = db_model.get_one_product(id)
		if not product_id:
			return {"messages": "Product was not found!"}, 404
		else:
			return product, 200



class StoreCategories(Resource):
	"""The store categories class."""

	@jwt_required
	def post(self, category_name):
		"""Add a category to the store."""
		parser = reqparse.RequestParser()
		parser.add_argument('category_name',
			type=str,
			required=True,
			help="Category name cannot be left blank!"
		)
		args = parser.parse_args()
		print(args['category_name'])
		category_name = db_model.add_category(args['category_name'])
		if category_name:
			return {'message': 'Uh-oh category with {} already exists'.format(category_name)}, 409
		return {'message': "Category has been added successfuly"}, 201


class OneCategory(Resource):
	"""One category class."""

	def get(self, id):
		"""Get one category from the store."""
		parser = reqparse.RequestParser()
		parser.add_argument('category_id',
			type=int,
			required=True,
			help="Category id cannot be left blank!"
		)
		category_id = db_model.category_id(id)
		return category_id


class StoreSales(Resource):
	"""This is a store sale class."""

	@jwt_required
	def post(self):
		"""Add a sale order to the store."""
		parser = reqparse.RequestParser()
		parser.add_argument('product_id',
			type=str,
			required=True,
			help="Product id cannot be left blank!"
		)
		parser.add_argument('quantity',
			type=int,
			required=True,
			help="Quantity cannot be left blank!"
		)
		parser.add_argument('user_id',
			type=str,
			required=True,
			help="User is cannot be left blank!"
		)
		args = parser.parse_args()
		product_id = args['product_id']
		quantity = args['quantity']
		user_id = args['user_id']
