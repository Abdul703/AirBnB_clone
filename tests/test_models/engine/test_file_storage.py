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
        self.file_path = 'file.json'
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test the all method."""
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Test the new method."""
        obj = BaseModel()
        self.storage.new(obj)
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key]['id'], obj.id)

    def test_save(self):
        """Test the save method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open(self.file_path, 'r', encoding='utf-8') as f:
            objects = json.load(f)
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.assertIn(key, objects)
        self.assertEqual(objects[key]['id'], obj.id)

    def test_reload(self):
        """Test the reload method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key]['id'], obj.id)

    def test_save_and_reload(self):
        """Test save and reload methods together."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key]['id'], obj.id)

if __name__ == '__main__':
    unittest.main()
