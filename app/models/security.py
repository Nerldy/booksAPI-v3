from .user import User

users = [User('bob', 'bob@mail.com', '123')]  # creates a dummy user

username_mapping = {u.user_name: u for u in users}  # creates a user mapping object using the user's name

user_id_mapping = {u.id: u for u in users}  # creates a user mapping object using the user's id


def authenticate(username, password):
	user = username_mapping.get(username, None)  # looks up user

	if user and user.password == password:
		return user


def identity(payload):
	user_id = payload['identity']
	return user_id_mapping.get(user_id, None)
