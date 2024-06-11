#!/usr/bin/python3
"""Unit tests for the User class."""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_class_attributes(self):
        """Test that User class attributes exist and are of correct type."""
        self.assertTrue(hasattr(User, 'email'))
        self.assertTrue(hasattr(User, 'password'))
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(hasattr(User, 'last_name'))
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)

    def test_instance_attributes(self):
        """Test that User instance attributes are initialized correctly."""
        user = User()
        self.assertEqual(user.email, '')
        self.assertEqual(user.password, '')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')

    def test_inheritance(self):
        """Test that User class inherits from BaseModel."""
        user = User()
        self.assertIsInstance(user, BaseModel)


if __name__ == '__main__':
    unittest.main()
