#!/usr/bin/python3
"""Command Prompt Module"""
import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
