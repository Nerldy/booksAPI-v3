import uuid
import datetime


class User:

	def __init__(self, user_name=None, user_email=None, password=None):
		self.id = uuid.uuid4()
		self.user_name = user_name
		self.user_email = user_email
		self.password = password
		self.is_admin = False
		self.date_created = datetime.datetime.now()

	def get_id(self):
		return self.id

	def get_user_name(self):
		return self.user_name

	def get_user_email(self):
		return self.user_email

	def get_password(self):
		return self.password

	def get_date_created(self):
		return self.date_created

	def serialize(self):
		return {
			"user_name": self.user_name,
			"id": self.id,
			"user_email": self.user_email,
			"is_admin": self.is_admin
		}
