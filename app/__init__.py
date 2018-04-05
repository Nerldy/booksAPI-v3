from flask import Flask, request, Response, jsonify, json, make_response, abort
from app.models.book import Book
from app.models.user import User
# from flask.ext.bcrypt import Bcrypt
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp


def authenticate(username, password):
	user = username_table.get(username, None)
	if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
		return user


def identity(payload):
	user_id = payload['identity']
	return userid_table.get(user_id, None)


"""
-------------
DUMMY OBJECTS
"""
users = [
	User(user_name='user1', user_email='user1@mail.com').set_password("1234"),
	User(user_name='user2', user_email='user2@mail.com').set_password("5678")
]

books_collection = []  # all books holder
users_collection = []  # all users holder
borrowed_books_collection = []  # borrowed books holder

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, authenticate, identity)


@app.route('/books')
def books_list():
	"""
	GET /books
	:return: All books
	"""

	if books_collection:
		return jsonify({"books": books_collection}), 200  # return dummy book list

	return jsonify({"message": "No books available"})


@app.route('/books', methods=['POST'])
def create_book():
	"""
	POST /books
	:return: Book created
	"""
	req_data = request.get_json()  # turn json into Python objects

	try:
		isbn_str = str(req_data['isbn'])

		if (req_data['title'] == "") or (req_data['title'].isspace()):  # check title is not empty
			return jsonify({"message": "Title can't be empty"}), 400

		if (req_data['isbn'] == "") or (req_data['isbn'].isspace()):  # check title is not empty
			return jsonify({"message": "isbn can't be empty"}), 400

		if (len(isbn_str) < 10) or (len(isbn_str) > 15):  # confirm length of isbn is 10 - 15
			return jsonify({"message": "isbn number must be between 10 - 15 characters"})

		if isinstance(req_data['author'], (list, str)) and (
				req_data['author'] != "" or req_data['author'].isspace()):  # confirm author is a list type
			print(req_data['author'])
			for book in books_collection:
				if book["isbn"] == req_data["isbn"]:  # check if book with the same ID number exists
					return jsonify({"message": 'Book already exists'}), 400  # return this if book exists

			book = Book(req_data['title'], req_data["isbn"])  # create book

			book.set_author(req_data['author'])  # create author list

			books_collection.append(book.serialize())  # add book to dummy book list

			return make_response(jsonify({"message": "Book has been created"}), 201)
	except KeyError:
		return jsonify({"message": "Couldn't understand your message, please try again"}), 400

	else:
		return jsonify({"message": "Author must be a list and can't be empty"})


@app.route('/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def book_id_item(book_id):
	"""
	GET, POST, DELETE to/from book collection
	:param book_id:
	:return: 200, 400, 404
	"""
	if book_id.isalnum():  # make sure book_id is web safe

		if request.method == 'DELETE':
			global books_collection
			books_collection = list(filter(lambda x: x["id"] != book_id, books_collection))
			return jsonify({"message": "book deleted"})

		if request.method == 'PUT':

			req_data = request.get_json()  # turn json into Python objects
			isbn_str = str(req_data['isbn'])  # turn isbn into a string

			if (req_data['title'] == "") or (req_data['title'].isspace()):  # check title is not empty
				return jsonify({"message": "Title can't be empty"}), 400

			if (req_data['isbn'] == "") or (req_data['isbn'].isspace()):  # check title is not empty
				return jsonify({"message": "isbn can't be empty"}), 400

			if (len(isbn_str) < 10) or (len(isbn_str) > 15):  # confirm length of isbn is 10 - 15
				return jsonify({"message": "isbn number must be between 10 - 15 characters"})

			if isinstance(req_data['author'], list):  # confirm author is a list type
				book = next(filter(lambda x: x["id"] == book_id, books_collection),
							None)  # search for book in collection

				if book is None:
					return jsonify({"message": "Book does not exist"})
				else:
					book.update(req_data)  # update book
					return jsonify({"message": "Book updated"})

			else:
				return jsonify({"message": "Author must be a list"})

		else:
			# GET function will run here

			book = next(filter(lambda x: x["id"] == book_id, books_collection), None)
			if book is None:
				return jsonify({"message": "Book does not exist"}), 404

			return jsonify({'book': book})

	return jsonify({"message": "You must use safe characters"})


@app.route('/users/books/<book_id>', methods=['POST'])
def user_borrow_book(book_id):
	"""
	POST to user collection if book exists in the book collection
	:param book_id:
	:return: 200, 404
	"""
	if book_id.isalnum():  # make sure book_id is web safe

		book = next(filter(lambda x: x["id"] == book_id, books_collection), None)
		if book is None:
			return jsonify({"message": "Book does not exist"}), 404

		borrowed_books_collection.append(book)

		return jsonify({"added book to your borrowed list": borrowed_books_collection})

	return jsonify({"message": "You must use safe characters"}), 404


"""
-----------------
AUTH

"""


@app.route('/auth/login', methods=['POST'])
def api_login():
	pass


@app.route('/register', methods=['POST'])
def api_register():
	username = request.json.get('user_name')
	password = request.json.get("password")
	email = request.json.get("user_email")

	if username is None or password is None:
		abort(400)

	for user in users_collection:
		if user['user_name'] == username:
			abort(404)
		else:
			new_user = User(username, email)
			new_user.set_password(password)
			users_collection.append(new_user)
			return jsonify({"message": f"hello {username}. Your account has been created"})


@app.route('/logout', methods=['POST'])
def api_logout():
	pass


@app.route('/reset-password', methods=['POST'])
def reset_password():
	pass
