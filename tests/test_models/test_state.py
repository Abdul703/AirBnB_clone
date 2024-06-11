#!/usr/bin/python3
"""Unit tests for the State class."""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_class_attributes(self):
        """Test that State class attribute exist and is of correct type."""
        self.assertTrue(hasattr(State, 'name'))
        self.assertIsInstance(State.name, str)
        

    def test_instance_attributes(self):
        """Test that State instance attribute is initialized correctly."""
        state = State()
        self.assertEqual(state.name, '')

    def test_inheritance(self):
        """Test that State class inherits from BaseModel."""
        state = State()
        self.assertIsInstance(state, BaseModel)


if __name__ == '__main__':
    unittest.main()
