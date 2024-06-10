#!/usr/bin/python3
"""Command Prompt Module"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command prompt class for HBNB.

    This class provides an interactive command line interface for HBNB.
    """

    prompt = '(hbnb) '

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

        if arg == 'BaseModel':
            obj = BaseModel()
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
        if class_name != 'BaseModel':
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
        if class_name != 'BaseModel':
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
            found = False

            for key, value in all_objects.items():
                if key.split('.')[0] == class_name:
                    found = True
                    print(value)
            
            if not found:
                print("** class doesn't exist **")

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
        if class_name != 'BaseModel':
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
          

if __name__ == '__main__':
    HBNBCommand().cmdloop()
