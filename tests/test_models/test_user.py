#!/usr/bin/python3
"""Test suite for User class."""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        """Set up test methods."""
        self.user = User()

    def test_inheritance(self):
        """Test that User inherits from BaseModel."""
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """Test that User has the correct attributes."""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertEqual(self.user.email, "")
        self.assertTrue(hasattr(self.user, "password"))
        self.assertEqual(self.user.password, "")
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertEqual(self.user.first_name, "")
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.last_name, "")

    def test_str(self):
        """Test the __str__ method."""
        string = str(self.user)
        self.assertIn("[User]", string)
        self.assertIn(f"({self.user.id})", string)
        self.assertIn("'email': ''", string)
        self.assertIn("'password': ''", string)
        self.assertIn("'first_name': ''", string)
        self.assertIn("'last_name': ''", string)

    def test_to_dict(self):
        """Test the to_dict method."""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], '')
        self.assertEqual(user_dict['password'], '')
        self.assertEqual(user_dict['first_name'], '')
        self.assertEqual(user_dict['last_name'], '')

    def test_kwargs(self):
        """Test initialization with kwargs."""
        new_user = User(email="test@test.com", password="1234", first_name="John", last_name="Doe")
        self.assertEqual(new_user.email, "test@test.com")
        self.assertEqual(new_user.password, "1234")
        self.assertEqual(new_user.first_name, "John")
        self.assertEqual(new_user.last_name, "Doe")


if __name__ == '__main__':
    unittest.main()
