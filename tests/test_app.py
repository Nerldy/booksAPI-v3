from app import app
import unittest


class HelloBooksAPITestCase(unittest.TestCase):
	def test_get_books(self):
		tester = app.test_client(self)
		response = tester.get('/books', content_type='application/json')
		self.assertEqual(response.status_code, 200)

	def test_put_works(self):
		tester = app.test_client(self)
		response = tester.put('/books', content_type='application/json')
		self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
	unittest.main()
