"""Local import."""
from .user import User

"""Create a list of users."""
users = [
    User(1, 'admin', 'admin'), (2, 'john', 'johndoe')
]

"""Find a user using their username."""
username_mapping = {u.username: u for u in users}
"""Find a user using their id."""
userid_mapping = {u.id: u for u in users}


"""Let us authenticate a user"""
def authentify(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user

def identify(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
