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
        """Create a BaseModel object and save it in file.json."""
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
        """Show the string representation of an instance based on the class name and id."""
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
