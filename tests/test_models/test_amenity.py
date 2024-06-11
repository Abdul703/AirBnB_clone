#!/usr/bin/python3
"""Unit tests for the Amenity class."""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_class_attributes(self):
        """Test that Amenity class attributes exist and are of correct type."""
        self.assertTrue(hasattr(Amenity, 'name'))
        self.assertIsInstance(Amenity.name, str)

    def test_instance_attributes(self):
        """Test that Amenity instance attributes are initialized correctly."""
        amenity = Amenity()
        self.assertEqual(amenity.name, '')

    def test_inheritance(self):
        """Test that Amenity class inherits from BaseModel."""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)


if __name__ == '__main__':
    unittest.main()
