#!/usr/bin/python3
"""Unit tests for the City class."""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_class_attributes(self):
        """Test that City class attributes exist and are of correct type."""
        self.assertTrue(hasattr(City, 'name'))
        self.assertTrue(hasattr(City, 'state_id'))
        self.assertIsInstance(City.name, str)
        self.assertIsInstance(City.state_id, str)

    def test_instance_attributes(self):
        """Test that City instance attributes are initialized correctly."""
        city = City()
        self.assertEqual(city.name, '')
        self.assertEqual(city.state_id, '')

    def test_inheritance(self):
        """Test that City class inherits from BaseModel."""
        city = City()
        self.assertIsInstance(city, BaseModel)


if __name__ == '__main__':
    unittest.main()
