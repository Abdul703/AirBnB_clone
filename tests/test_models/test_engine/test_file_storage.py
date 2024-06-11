#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage
import os
import json


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.file_path = storage._FileStorage__file_path
        self.objects = storage._FileStorage__objects
        self.base_model = BaseModel()
        self.user = User()
        self.state = State()
        self.city = City()
        self.place = Place()
        self.amenity = Amenity()
        self.review = Review()
        self.objects.clear()

    def tearDown(self):
        """Tear down test environment."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.objects.clear()

    def test_all(self):
        """Test the all method."""
        self.assertEqual(storage.all(), self.objects)
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        """Test the new method."""
        storage.new(self.base_model)
        key = f'BaseModel.{self.base_model.id}'
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key], self.base_model)

    def test_save(self):
        """Test the save method."""
        storage.new(self.base_model)
        storage.save()
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        key = f'BaseModel.{self.base_model.id}'
        self.assertIn(key, data)
        self.assertEqual(data[key]['id'], self.base_model.id)

    def test_reload(self):
        """Test the reload method."""
        storage.new(self.base_model)
        storage.save()
        storage.reload()
        key = f'BaseModel.{self.base_model.id}'
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key].id, self.base_model.id)

    def test_classes_in_storage(self):
        """Test the various classes are properly handled by storage."""
        classes = [self.base_model, self.user, self.state, self.city, self.place, self.amenity, self.review]
        for obj in classes:
            storage.new(obj)
            key = f'{obj.__class__.__name__}.{obj.id}'
            self.assertIn(key, storage.all())
            self.assertEqual(storage.all()[key], obj)
        storage.save()
        storage.reload()
        for obj in classes:
            key = f'{obj.__class__.__name__}.{obj.id}'
            self.assertIn(key, storage.all())
            self.assertEqual(storage.all()[key].id, obj.id)


if __name__ == '__main__':
    unittest.main()
