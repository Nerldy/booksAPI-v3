import unittest
from app.models.book import Book


class BookTestCase(unittest.TestCase):
	"""this class tests Book class"""

	def setUp(self):
		self.book = Book()

	def test_title_is_not_none(self):
		res = self.book.title
		self.assertIsNotNone(res)

	def test_isbn_is_not_none(self):
		res = self.book.isbn
		self.assertIsNotNone(res)

	def test_author_is_a_list_type(self):
		res = isinstance(self.book.author, list)
		self.assertEqual(res, True)

	def test_id_is_hex(self):
		res = isinstance(self.book.id, int)
		self.assertEqual(res, False)


if __name__ == '__main__':
	unittest.main()
