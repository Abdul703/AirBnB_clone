#!/usr/bin/python3
"""FileStorage class module."""
import json
from os.path import exists


class FileStorage:
    """FileStorage class for serialization and deserialization
    of objects to and from a JSON file.
    """

    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """Initialize the FileStorage instance."""
        pass

    def all(self):
        """Return all saved objects.

        Returns:
            dict: Dictionary of all saved objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Set a new object in the storage.

        Args:
            obj (object): The object to set.
        """
        key = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """Serialize and save objects to the JSON file."""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """Deserialize the JSON file to objects."""
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                FileStorage.__objects = json.load(f)
