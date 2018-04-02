import uuid
import datetime


class User:

	def __init__(self, username, useremail, password):
		self.id = uuid.uuid4()
		self.username = username
		self.email = useremail
		self.password = password
		self.date_created = datetime.datetime.now()

	def get_id(self):
		return self.id

	def get_username(self):
		return self.username

	def get_email(self):
		return self.email

	def get_password(self):
		return self.password

	def get_date_created(self):
		return self.date_created
