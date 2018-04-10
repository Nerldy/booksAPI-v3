from app import app
from flask import json
import unittest
from app.models.user import User


class AuthTestCases(unittest.TestCase):
	"""this class tests Auth"""

	def setUp(self):
		"""sets up app"""
		app.testing = True
		self.app = app.test_client()
		self.user = User('bob', 'bob@mail.com')

	def tearDown(self):
		"""removes app"""
		app.testing = False
		self.app = None

	def test_login_password_is_not_longer_than_8(self):
		payload = {
			"user_name": "don",
			"user_email": "don@mail.com",
			"password": "12345"
		}

		res = self.app.post("/auth/login", data=json.dumps(payload), content_type="application/json")
		assert b"Password must be longer than 8 characters" in res.data

	def test_login_password_is_successful(self):
		payload = {
			"user_name": "don",
			"user_email": "don@mail.com",
			"password": "123457890"
		}

		res = self.app.post("/auth/login", data=json.dumps(payload), content_type="application/json")
		assert b"please create a new account" in res.data

	def test_login_username_is_not_empty(self):
		payload = {
			"user_name": "",
			"user_email": "don@mail.com",
			"password": "123457890"
		}

		res = self.app.post("/auth/login", data=json.dumps(payload), content_type="application/json")
		assert b"username and/or email fields cannot be empty" in res.data

	def test_login_username_empty_json_returns_message(self):
		payload = {}

		res = self.app.post("/auth/login", data=json.dumps(payload), content_type="application/json")
		assert b"Make sure username, password and email fields are provided " in res.data
