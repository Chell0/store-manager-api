from flask_restful import Resource, reqparse
from werkzeug.exceptions import BadRequest, NotFound, Unauthorized

import re

# local imports
from api.app.v2.store.model import StoreDb

db_model = StoreDb()

class StoreProducts(Resource):
	"""Store products class."""
	@auth_required
	def post(self):
		"""Add a product to the store."""
		parser = reqparse.RequestParser()
		parser.add_argument('product_name',
			type=str,
			required=True,
			help="Product name cannot be left blank!"
		)
		parser.add_argument('stock',
			type=str,
			required=True,
			help="Stock status cannot be left blank!"
		)
		parser.add_argument('price',
			type=int,
			required=True,
			help="Price cannot be left blank!"
		)
		parser.add_argument('category_name',
			type=str,
			required=True,
			help="Category name cannot be left blank!"
		)
		args = parser.parse_args()
		product_name = db_model.get_one_product(args['product_name'])
		category_name = db_model.get_one_category(args['category_name'])

	def get(self):
		"""Fetch all products."""
		products = db_model.get_all_products()
		if len(products) <= 0:
			return {"message": "Sorry, there are no products"}, 200
		else:
			all_products = {}
			for p in products:
				all_products.append(product)


	def put(self, id):
		"""Modify a product."""
		parser = reqparse.RequestParser()
		parse.add_argument('stock',
			type=str,
			required=True,
			help="Stock cannot be left blank!"
		)
		args = parser.parse_args()
		product = db_model.modify_a_product(id)


	def delete(self, id):
		"""Delete a product."""
		product = db_model.get_one_product(id)
		product_id = db_model.delete_a_category(id)
		if product:
			return {"messages": "Product was deleted successfully!"}, 204
		else:
			return {"message": "Product was not found"}, 404

