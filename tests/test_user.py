import unittest
from app.models.user import User


class UserTestCase(unittest.TestCase):

	def setUp(self):
		self.user = User('tester', 'tester@email.com')

	def test_verify_hashed_password(self):
		pswd = self.user.set_password("1234")
		hashed = self.user.verify_password('1234')
		return self.assertEqual(hashed, True)

	def test_verify_hashed_password_returns_false(self):
		pswd = self.user.set_password("1234")
		hashed = self.user.verify_password('456')
		return self.assertEqual(hashed, False)
