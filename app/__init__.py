from flask import Flask, request, Response, jsonify, json
from app.models.book import Book
from app.models.user import User

app = Flask(__name__)
books_collection = []


@app.route('/books')
def books_list():
	"""

	:return: All books
	"""

	return jsonify({"books": books_collection}), 200  # return dummy book list


@app.route('/books', methods=['POST'])
def create_book():
	"""

	:return: Book created
	"""
	req_data = request.get_json()  # turn json into Python objects

	for book in books_collection:
		if book['isbn'] == req_data['isbn']:  # check if book with the same ISBN number exists
			return jsonify({"message": 'Book already exists'}), 400  # return this if book exists

	book = Book(req_data['title'], req_data['isbn'])

	for author in req_data['author']:
		book.set_author(author)  # create author list

	books_collection.append(book.serialize())  # add book to dummy book list

	return jsonify({"message": "Book has been created"}), 201


@app.route('/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def book_id_item(book_id):
	if request.method == 'PUT':
		pass


@app.route('/users/books/<book_id>', methods=['POST'])
def user_borrow_book(book_id):
	return 'Borrow' + book_id
