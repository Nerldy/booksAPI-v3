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
		self.book = Book(title='The Wave Rain', isbn='A5-45CKWELO556-998')

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


if __name__ == '__main__':
	unittest.main()
