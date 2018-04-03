import uuid
import datetime


class Book:

	def __init__(self, title="", isbn=""):
		self.id = uuid.uuid4()
		self.title = title
		self.isbn = isbn
		self.author = []
		self.date_created = datetime.datetime.now()

	def get_book_id(self):
		return self.id

	def get_title(self):
		return self.title

	def set_author(self, name):
		self.author.append(name)

	def get_author(self):
		return self.author

	def get_date_created(self):
		return self.date_created

	def serialize(self):
		return {
			"id": self.id,
			"title": self.title,
			"isbn": self.isbn,
			"author": self.author,
			"date_created": self.date_created
		}
