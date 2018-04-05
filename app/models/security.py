from .user import User

users = [
	User('bob', 'bob@mail.com', '123')
]

username_mapping = {
	"bob": {
		"id": 1,
		"user_name": "bob",
		"password": 123,
		"email": "user@email.com"
	}
}

user_id_mapping = {
	1: {
		"id": 1,
		"user_name": "bob",
		"password": 123,
		"email": "user@email.com"
	}
}


def authenticate(username, password):
	user = username_mapping.get(username, None)  # looks up user

	if user and user.password == password:
		return user


def identity(payload):
	user_id = payload['identity']
	return user_id_mapping.get(user_id, None)
