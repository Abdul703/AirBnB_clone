#!/usr/bin/python3
"""
Unit tests for BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Test suite for the BaseModel class."""

    def setUp(self):
        """Set up test environment."""
        self.model = BaseModel()

    def tearDown(self):
        """Clean up after tests."""
        try:
            storage._FileStorage__objects.clear()
        except AttributeError:
            pass

    def test_init(self):
        """Test initialization of BaseModel."""
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))

    def test_str(self):
        """Test the __str__ method."""
        string_representation = str(self.model)
        self.assertIn("[BaseModel]", string_representation)
        self.assertIn(f"({self.model.id})", string_representation)
        self.assertIn(f"'id': '{self.model.id}'", string_representation)

    def test_save(self):
        """Test the save method."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method."""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

    def test_kwargs(self):
        """Test initialization with kwargs."""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)
        self.assertNotIn('__class__', new_model.__dict__)


if __name__ == '__main__':
    unittest.main()
