import re

from werkzeug.exceptions import BadRequest, NotFound

class Validate:
	"""Validate class."""

	def validate_email(self, email):
		"""Validate the email address."""
		if not re.match(r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", email):
			raise BadRequest("This is not a valid email address")
		return email

	def validate_password(self, password):
		"""Validate password length."""
		if len(password) < 4:
			raise BadRequest("Password is too short, minimum is 8 characters")
		elif len(password) < 8:
			raise BadRequest("Password is too short, minimum is 8 characters")
		elif len(password) > 16:
			raise BadRequest("Password is too long, maximum is 12 characters")
		else:
			return password

