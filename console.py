#!/usr/bin/python3
"""
Command Prompt Module

This module defines the HBNBCommand class, which provides an interactive command line interface 
for managing HBNB instances. It allows users to create, show, destroy, update, and list instances 
of various classes defined in the HBNB project.

Classes:
    HBNBCommand: Command prompt class for HBNB.

Usage:
    Run this module directly to start the HBNB command line interface.
    Example:
        $ ./console.py
"""
import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Command prompt class for HBNB.

    This class provides an interactive command line interface for HBNB.
    """

    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Place': Place,
        'Amenity': Amenity,
        'Review': Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Handle EOF (CTRL+D) to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, arg):
        """
        Create a BaseModel object and save it in file.json.

        Syntax:
            create <class name>
        """
        if not arg:
            print("** class name missing **")
            return

        if arg in self.classes:
            obj = self.classes[arg]()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Show the string representation of an instance based on the
        class name and id.

        Syntax:
            show <class name> <id>
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_id = args[1]

        all_objects = storage.all()
        key = f'{class_name}.{obj_id}'

        try:
            obj = all_objects[key]
            print(obj)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.

        Syntax:
            destroy <class name> <id>
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_id = args[1]

        all_objects = storage.all()
        key = f'{class_name}.{obj_id}'

        try:
            del all_objects[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the
        class name.

        Syntax:
            all <class name (optional)>
        """

        args = arg.split()
        all_objects = storage.all()

        if len(args) == 0:
            # No class name provided, print all objects
            for obj in all_objects.values():
                print(obj)
        else:
            # Class name provided, filter and print objects of that class
            class_name = args[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return

            for key, value in all_objects.items():
                if key.split('.')[0] == class_name:
                    print(value)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by
           adding or updating attribute

        Syntax:
            update <class name> <id> <attribute name> "<attribute value>"
        """

        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_id = args[1]
        
        all_objects = storage.all()
        key = f'{class_name}.{obj_id}'

        try:
            obj = all_objects[key]
            if len(args) == 2:
                print("** attribute name missing **")
                return
            if len(args) == 3:
                print("** value missing **")
                return

            attr_name, attr_value = args[2], args[3].strip('"')
            if hasattr(obj, attr_name):
                attr_type = type(getattr(obj, attr_name))
                setattr(obj, attr_name, attr_type(attr_value))
            else:
                setattr(obj, attr_name, attr_value)
            obj.save()

        except KeyError:
            print("** no instance found **")

    def default(self, line):
        """
        Handle <class name>.<command>() syntax.

        This method intercepts commands that are not explicitly handled
        and checks if they match the <class name>.<command>() pattern.
        """
        parts = line.split('.')
        class_name, method_call = parts[0], parts[1]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        method_name, method_args = method_call.split('(')
        method_args = method_args.rstrip(')')

        if method_name == 'all':
            self.do_all(class_name)
        elif method_name == 'count':
            all_objects = storage.all().keys()
            class_objs = [k for k in all_objects if k.startswith(class_name)]
            print(len(class_objs))
        elif method_name == 'show':
            id = method_args
            arg = f"{class_name} {id}"
            self.do_show(arg)
        elif method_name == 'destroy':
            id = method_args
            arg = f"{class_name} {id}"
            self.do_destroy(arg)
          

if __name__ == '__main__':
    HBNBCommand().cmdloop()
