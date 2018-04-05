from flask import Flask, request, Response, jsonify, json, make_response
from app.models.book import Book
from app.models.user import User
# from flask.ext.bcrypt import Bcrypt
from flask_jwt import JWT, jwt_required
from .models.security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'test'
# bcrypt = Bcrypt(app)
jwt = JWT(app, authenticate, identity)

"""
-------------
DUMMY OBJECTS
"""
books_collection = []  # initialize empty books list
users_collection = []  # initialize empty users list


@app.route('/books')
def books_list():
	"""

	:return: All books
	"""

	if books_collection:
		return jsonify({"books": books_collection}), 200  # return dummy book list

	return jsonify({"message": "No books available"})


@app.route('/books', methods=['POST'])
def create_book():
	"""

	:return: Book created
	"""
	req_data = request.get_json()  # turn json into Python objects
	isbn_str = str(req_data['isbn'])

	if (req_data['title'] == "") or (req_data['title'].isspace()):  # check title is not empty
		return jsonify({"message": "Title can't be empty"}), 400

	if (req_data['isbn'] == "") or (req_data['isbn'].isspace()):  # check title is not empty
		return jsonify({"message": "isbn can't be empty"}), 400

	if (len(isbn_str) < 10) or (len(isbn_str) > 15):  # confirm length of isbn is 10 - 15
		return jsonify({"message": "isbn number must be between 10 - 15 characters"})

	if isinstance(req_data['author'], list):  # confirm author is a list type
		for book in books_collection:
			if book["isbn"] == req_data["isbn"]:  # check if book with the same ID number exists
				return jsonify({"message": 'Book already exists'}), 400  # return this if book exists

		book = Book(req_data['title'], req_data["isbn"])  # create book

		for author in req_data['author']:
			book.set_author(author)  # create author list

		books_collection.append(book.serialize())  # add book to dummy book list

		return jsonify({"message": "Book has been created"}), 201

	else:
		return jsonify({"message": "Author must be a list"})


@app.route('/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def book_id_item(book_id):
	if book_id.isalnum():  # make sure book_id is web safe

		if request.method == 'DELETE':
			global books_collection
			books_collection = list(filter(lambda x: x["id"] != book_id, books_collection))
			return jsonify({"message": "book deleted"})

		if request.method == 'PUT':
			req_data = request.get_json()
			book = next(filter(lambda x: x["id"] == book_id, books_collection), None)  # search for book in collection

			if book is None:
				return jsonify({"message": "Book does not exist"})
			else:
				book.update(req_data)
				return jsonify({"message": "Book updated"})

		else:
			# GET function will run here

			book = next(filter(lambda x: x["id"] == book_id, books_collection), None)
			if book is None:
				return jsonify({"message": "Book does not exist"}), 404

			return jsonify({'book': book}), 200

	return jsonify({"message": "You must use safe characters"})


@app.route('/users/books/<book_id>', methods=['POST'])
def user_borrow_book(book_id):
	return 'Borrow' + book_id


"""
-----------------
AUTH

"""


@app.route('/login', methods=['POST'])
@jwt_required()
def api_login():
	pass


@app.route('/register', methods=['POST'])
def api_register():
	pass


@app.route('/logout', methods=['POST'])
def api_logout():
	pass


@app.route('/reset-password', methods=['POST'])
def reset_password():
	pass
