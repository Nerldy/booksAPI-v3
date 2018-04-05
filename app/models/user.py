import uuid
import datetime
from passlib.apps import custom_app_context as pwd_context


class User:

	def __init__(self, user_name, user_email):
		self.id = uuid.uuid4().hex
		self.user_name = user_name
		self.user_email = user_email
		self.password = None
		self.is_admin = False
		self.date_created = datetime.datetime.now()

	def set_password(self, password):
		self.password = pwd_context.encrypt(password)

	def verify_password(self, password):
		return pwd_context.verify(password, self.password)

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
