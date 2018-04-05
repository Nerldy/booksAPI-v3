from app import app
from flask import json
import unittest
from app.models.book import Book
from app.models.user import User


class HelloBooksAPITestCase(unittest.TestCase):
	"""This class tests Flask CRUD functions"""

	def setUp(self):
		"""sets up app"""
		app.testing = True
		self.app = app.test_client()
		self.book = Book(title='The Wave Rain', isbn='1234567890')

	def tearDown(self):
		"""removes app"""
		app.testing = False
		self.app = None

	def test_get_books_list(self):
		"""
		Tests GET /books returns a list
		:return: 200
		"""
		resp = self.app.get('/books')
		self.assertEqual(resp.status_code, 200)

	def test_create_book(self):
		"""
		Tests Create book API endpoint
		Asserts 201 Created Status Code Response
		"""
		#
		payload = {
			"title": "New Book",
			"author": "New Author",
			"isbn": "12345678901"
		}

		res = self.app.post('/books', data=json.dumps(payload), content_type="application/json")
		return self.assertEqual(res.status_code, 201)

	def test_no_book_400_bad_request_error(self):
		"""
		test empty object
		:return: 400
		"""
		payload = {}

		res = self.app.post('/books', data=json.dumps(payload), content_type="application/json")
		return self.assertEqual(res.status_code, 400)

	def test_create_book_empty_object_raises_key_error(self):
		"""
		tests key error is raised
		:return: KeyError
		"""
		payload = {}

		res = self.app.post('/books', data=json.dumps(payload), content_type="application/json")
		return self.assertRaises(KeyError)

	def test_forward_slash_does_not_throw_404_error(self):
		res = self.app.get("books/")
		self.assertEqual(res.status_code, 200)

	def test_empty_title_is_required(self):
		"""
		checks if title is empty
		:return: message string
		"""
		payload = {
			"title": "",
			"author": "New Author",
			"isbn": "12345678901"
		}

		res = self.app.post('/books', data=json.dumps(payload), content_type="application/json")
		assert b"Title can't be empty" in res.data

	def test_title_is_not_spaced(self):
		"""
		checks if title is empty
		:return: message string
		"""
		payload = {
			"title": "            ",
			"author": "New Author",
			"isbn": "12345678901"
		}

		res = self.app.post('/books', data=json.dumps(payload), content_type="application/json")
		assert b"Title can't be empty" in res.data

	def test_isbn_is_not_an_empty_string(self):
		"""
		checks isbn field is not empty
		:return: message string
		"""
		payload = {
			"title": "Hello",
			"author": "tester",
			"isbn": ""
		}

		res = self.app.post('/books', data=json.dumps(payload), content_type="application/json")
		assert b"isbn can't be empty" in res.data

	def test_isbn_is_not_less_than_10(self):
		payload = {
			"title": "Hello",
			"author": "Helo",
			"isbn": "12364"
		}

		res = self.app.post('/books', data=json.dumps(payload), content_type="application/json")
		assert b"isbn number must be between 10 - 15 characters" in res.data

	def test_isbn_is_not_more_than_15(self):
		payload = {
			"title": "Hello",
			"author": "Helo",
			"isbn": "1234567890123456"
		}

		res = self.app.post('/books', data=json.dumps(payload), content_type="application/json")
		assert b"isbn number must be between 10 - 15 characters" in res.data

	def test_author_is_not_empty(self):
		payload = {
			"title": "Hello",
			"author": "",
			"isbn": "1234567890"
		}

		res = self.app.post('/books', data=json.dumps(payload), content_type="application/json")
		assert b"Author must be a list and can't be empty" in res.data

	def test_get_all_books_returns_books_not_available(self):
		res = self.app.get('/books')
		one = len(res.data) > 0
		return self.assertEqual(one, True)

	def test_delete_book_returns_success_message(self):
		book_id = self.book.get_book_id()
		res = self.app.delete('/books/' + book_id)
		assert b"book deleted" in res.data


if __name__ == '__main__':
	unittest.main()
