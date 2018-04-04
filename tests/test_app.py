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

		payload = {
			"title": "New Book",
			"author": "New Author",
			"isbn": "389837"
		}

		res = self.app.post('/books', data=json.dumps(payload))
		return self.assertEqual(res.status_code, 201)


if __name__ == '__main__':
	unittest.main()
