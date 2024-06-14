#!/usr/bin/python3
"""
Unit tests for the HBNBCommand class
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
import os

from models.state import State
from models.user import User

class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class"""

    def setUp(self):
        """Set up for tests"""
        self.cli = HBNBCommand()
        self.classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Place': Place,
            'Amenity': Amenity,
            'Review': Review
        }

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove("file.json")
        except Exception:
            pass
        storage.all().clear()

    def test_quit(self):
        """Test the quit command"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("quit")
            self.assertEqual(output.getvalue(), "")

    def test_EOF(self):
        """Test the EOF command"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("EOF")
            self.assertEqual(output.getvalue(), "\n")

    def test_emptyline(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("")
            self.assertEqual(output.getvalue(), "")

    def test_help(self):
        """Test help command for all commands"""
        command_helps = {
            'help': 'List available commands with "help" or detailed help with "help cmd".',
            'EOF': 'Handle EOF (CTRL+D) to exit the program.',
        }

        for cmd, msg in command_helps.items():
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"help {cmd}")
                self.assertIsInstance(f.getvalue(), str)
                self.assertEqual(f.getvalue().strip(), msg)


    def test_create_missing_class(self):
        """Test create command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("create")
            self.assertEqual(output.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class(self):
        """Test create command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("create InvalidClass")
            self.assertEqual(output.getvalue().strip(), "** class doesn't exist **")

    def test_create_valid_class(self):
        """Test create command with valid class name"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("create BaseModel")
            obj_id = output.getvalue().strip()
            self.assertTrue(f'BaseModel.{obj_id}' in storage.all().keys())

    def test_show_missing_class(self):
        """Test show command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("show")
            self.assertEqual(output.getvalue().strip(), "** class name missing **")

    def test_show_invalid_class(self):
        """Test show command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("show InvalidClass")
            self.assertEqual(output.getvalue().strip(), "** class doesn't exist **")

    def test_show_missing_id(self):
        """Test show command with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("show BaseModel")
            self.assertEqual(output.getvalue().strip(), "** instance id missing **")

    def test_show_invalid_id(self):
        """Test show command with invalid instance id"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("show BaseModel invalid_id")
            self.assertEqual(output.getvalue().strip(), "** no instance found **")

    def test_show_valid_instance(self):
        """Test show command with valid class name and instance id"""
        with patch('sys.stdout', new=StringIO()) as output:
            obj = BaseModel()
            obj.save()
            self.cli.onecmd(f"show BaseModel {obj.id}")
            self.assertIn(str(obj), output.getvalue())

    def test_destroy_missing_class(self):
        """Test destroy command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("destroy")
            self.assertEqual(output.getvalue().strip(), "** class name missing **")

    def test_destroy_invalid_class(self):
        """Test destroy command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("destroy InvalidClass")
            self.assertEqual(output.getvalue().strip(), "** class doesn't exist **")

    def test_destroy_missing_id(self):
        """Test destroy command with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("destroy BaseModel")
            self.assertEqual(output.getvalue().strip(), "** instance id missing **")

    def test_destroy_invalid_id(self):
        """Test destroy command with invalid instance id"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("destroy BaseModel invalid_id")
            self.assertEqual(output.getvalue().strip(), "** no instance found **")

    def test_destroy_valid_instance(self):
        """Test destroy command with valid class name and instance id"""
        with patch('sys.stdout', new=StringIO()) as output:
            obj = BaseModel()
            obj.save()
            self.cli.onecmd(f"destroy BaseModel {obj.id}")
            self.assertNotIn(f"BaseModel.{obj.id}", storage.all())

    def test_all_invalid_class(self):
        """Test all command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("all InvalidClass")
            self.assertEqual(output.getvalue().strip(), "** class doesn't exist **")

    def test_all_valid_class(self):
        """Test all command with valid class name"""
        with patch('sys.stdout', new=StringIO()) as output:
            obj = BaseModel()
            obj.save()
            self.cli.onecmd("all BaseModel")
            self.assertIn(str(obj), output.getvalue())

    def test_all_no_class(self):
        """Test all command with no class name"""
        with patch('sys.stdout', new=StringIO()) as output:
            obj = BaseModel()
            obj.save()
            self.cli.onecmd("all")
            self.assertIn(str(obj), output.getvalue())

    def test_update_missing_class(self):
        """Test update command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("update")
            self.assertEqual(output.getvalue().strip(), "** class name missing **")

    def test_update_invalid_class(self):
        """Test update command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("update InvalidClass")
            self.assertEqual(output.getvalue().strip(), "** class doesn't exist **")

    def test_update_missing_id(self):
        """Test update command with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("update BaseModel")
            self.assertEqual(output.getvalue().strip(), "** instance id missing **")

    def test_update_invalid_id(self):
        """Test update command with invalid instance id"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cli.onecmd("update BaseModel invalid_id")
            self.assertEqual(output.getvalue().strip(), "** no instance found **")

    def test_update_missing_attribute_name(self):
        """Test update command with missing attribute name"""
        with patch('sys.stdout', new=StringIO()) as output:
            obj = BaseModel()
            obj.save()
            self.cli.onecmd(f"update BaseModel {obj.id}")
            self.assertEqual(output.getvalue().strip(), "** attribute name missing **")

    def test_update_missing_value(self):
        """Test update command with missing value"""
        with patch('sys.stdout', new=StringIO()) as output:
            obj = BaseModel()
            obj.save()
            self.cli.onecmd(f"update BaseModel {obj.id} name")
            self.assertEqual(output.getvalue().strip(), "** value missing **")

    def test_update_valid(self):
        """Test update command with valid input"""
        with patch('sys.stdout', new=StringIO()) as output:
            obj = BaseModel()
            obj.save()
            self.cli.onecmd(f'update BaseModel {obj.id} name NewName')
            self.assertEqual(obj.name, "NewName")

    def test_class_name_dot_method_all(self):
        """Test <class name>.all() command"""
        for class_name in self.classes:
            with patch('sys.stdout', new=StringIO()) as output:
                obj = self.classes[class_name]()
                obj.save()
                self.cli.onecmd(f"{class_name}.all()")
                self.assertIn(str(obj), output.getvalue())

    def test_class_name_dot_method_count(self):
        """Test <class name>.count() command"""
        for class_name in self.classes:
            with patch('sys.stdout', new=StringIO()) as output:
                count = len([obj for obj in storage.all().values() if obj.__class__.__name__ == class_name])
                self.cli.onecmd(f"{class_name}.count()")
                self.assertEqual(output.getvalue().strip(), str(count))

    def test_class_name_dot_method_show(self):
        """Test <class name>.show(<id>) command"""
        for class_name, cls in self.classes.items():
            with patch('sys.stdout', new=StringIO()) as output:
                obj = cls()
                obj.save()
                self.cli.onecmd(f"{class_name}.show({obj.id})")
                self.assertIn(str(obj), output.getvalue())

    def test_class_name_dot_method_destroy(self):
        """Test <class name>.destroy(<id>) command"""
        for class_name, cls in self.classes.items():
            with patch('sys.stdout', new=StringIO()) as output:
                obj = cls()
                obj.save()
                self.cli.onecmd(f"{class_name}.destroy({obj.id})")
                self.assertNotIn(f"{class_name}.{obj.id}", storage.all())

    # def test_class_name_dot_method_update(self):
    #     """Test <class name>.update(<id>, <attribute name>, <attribute value>) command"""
    #     for class_name, cls in self.classes.items():
    #         with patch('sys.stdout', new=StringIO()) as output:
    #             obj = cls()
    #             obj.save()
    #             self.cli.onecmd(f'{class_name}.update({obj.id}, name, "NewName")')
    #             self.assertEqual(obj.name, "NewName")

    # def test_class_name_dot_method_update_dict(self):
    #     """Test <class name>.update(<id>, <dictionary representation>) command"""
    #     for class_name, cls in self.classes.items():
    #         with patch('sys.stdout', new=StringIO()) as output:
    #             obj = cls()
    #             obj.save()
    #             self.cli.onecmd(f'{class_name}.update({obj.id}, {{"name": "New Name", "age": 30}})')
    #             self.assertEqual(obj.name, "New Name")
    #             self.assertEqual(obj.age, 30)

if __name__ == '__main__':
    unittest.main()
