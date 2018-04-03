import unittest
from app.models.book import Book


class BookTestCase(unittest.TestCase):
	"""this class tests Book class"""

	def test_title_is_not_none(self):
		book = Book()
		res = book.title
		self.assertIsNotNone(res)

	def test_isbn_is_not_none(self):
		book = Book()
		res = book.isbn
		self.assertIsNotNone(res)

	def test_author_is_a_list_type(self):
		book = Book()
		res = isinstance(book.author, list)
		self.assertEqual(res, True)


if __name__ == '__main__':
	unittest.main()
