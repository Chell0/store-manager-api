from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

# local imports
from api.app.v2.security.validate import Validate as validate
from api.app.v2.auth.user_models import Authentication as usr



class UserRegistration(Resource):
	"""User registration class."""

	def post(self):

		parser = reqparse.RequestParser()
		parser.add_argument('user_name',
			type=str,
			required=True,
			help="Username cannot be left blank!"
		)
		parser.add_argument('email',
			type=str,
			required=True,
			help="Email cannot be left blank!"
		)
		parser.add_argument('password',
			type=str,
			required=True,
			help="Password cannot be left blank!"
		)
		args = parser.parse_args()
		username = args['user_name']
		email = args['email']
		password = args['password']
		data = [username, email, password]
		return usr.create_user(self, data)
		
		return (
			{
			"status": "success",
			"messages": "User sucessfully created!"
			}), 201


class UserLogin(Resource):
	"""User login class."""
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('email',
			type=str,
			required=True,
			help="Email cannot be left blank!"
		)
		parser.add_argument('password',
			type=str,
			required=True,
			help="Password cannot be left blank!"
		)
		args=parser.parse_args()
		email = args['email']
		password = args['password']
		user = usr.fetch_email(self, email)
		if password == user[0][3]:
			details = [user[0][0], user[0][1], user[0][4]]
			access_token = create_access_token(identity = details)
			return access_token, 200
		return {
			"message": "Error password does not match"
		}, 400


class CreateAttendantAccount(Resource):
	"""User store attendant account creation."""

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('user_name',
			type=str,
			required=True,
			help="Username cannot be left blank!"
		)
		parser.add_argument('email',
			type=str,
			required=True,
			help="Email cannot be left blank!"
		)
		parser.add_argument('password',
			type=str,
			required=True,
			help="Password cannot be left blank!"
		)
		args = parser.parse_args()
		email = args['email']
		password = args['password']
		user = usr.create_user(self, user_name, email, password)
		return {'message': 'User successfully created'}


class GiveAdminRights(Resource):
	"""Admin rights class."""

	def put(self):
		parser = reqparse.RequestParser()
		parser.add_argument('email',
			type=str,
			required=True,
			help="Please provide an email address for an update to occur"
		)
		args = parser.parse_args()
		email = args['email']



