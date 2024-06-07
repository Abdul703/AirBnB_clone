#!/usr/bin/python3
"""
Unit tests for FileStorage class.
"""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test suite for the FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.file_path = FileStorage._FileStorage__file_path
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.storage.new(self.obj)

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.storage._FileStorage__objects.clear()

    def test_all(self):
        """Test the all method."""
        self.assertEqual(self.storage.all(), {f"BaseModel.{self.obj.id}": self.obj})

    def test_new(self):
        """Test the new method."""
        new_obj = BaseModel()
        self.storage.new(new_obj)
        key = f"BaseModel.{new_obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test the save method."""
        self.storage.save()
        with open(self.file_path, 'r', encoding='utf-8') as f:
            objects = json.load(f)
        key = f"BaseModel.{self.obj.id}"
        self.assertIn(key, objects)
        self.assertEqual(objects[key]['id'], self.obj.id)

    def test_reload(self):
        """Test the reload method."""
        self.storage.save()
        self.storage._FileStorage__objects.clear()
        self.storage.reload()
        key = f"BaseModel.{self.obj.id}"
        self.assertIn(key, self.storage.all())
        reloaded_obj = self.storage.all()[key]
        self.assertEqual(reloaded_obj.id, self.obj.id)
        self.assertEqual(reloaded_obj.created_at, self.obj.created_at)
        self.assertEqual(reloaded_obj.updated_at, self.obj.updated_at)

    def test_save_and_reload(self):
        """Test save and reload methods together."""
        self.storage.save()
        self.storage._FileStorage__objects.clear()
        self.storage.reload()
        key = f"BaseModel.{self.obj.id}"
        self.assertIn(key, self.storage.all())
        reloaded_obj = self.storage.all()[key]
        self.assertEqual(reloaded_obj.id, self.obj.id)
        self.assertEqual(reloaded_obj.created_at, self.obj.created_at)
        self.assertEqual(reloaded_obj.updated_at, self.obj.updated_at)


if __name__ == '__main__':
    unittest.main()
