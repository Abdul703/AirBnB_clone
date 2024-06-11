#!/usr/bin/python3
"""FileStorage class module."""
import json
from os.path import exists
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize and save objects to the JSON file."""
        items = FileStorage.__objects.items()
        dict_to_save = {key: value.to_dict() for key, value in items}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(dict_to_save, file)

    def reload(self):
        """Deserialize the JSON file to objects."""
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                items = json.load(file)
                for key, value in items.items():
                    class_name = value['__class__']
                    if class_name == 'BaseModel':
                        FileStorage.__objects[key] = BaseModel(**value)
                    elif class_name == 'User':
                        FileStorage.__objects[key] = User(**value)
                    elif class_name == 'Place':
                        FileStorage.__objects[key] = Place(**value)
                    elif class_name == 'City':
                        FileStorage.__objects[key] = City(**value)
                    elif class_name == 'State':
                        FileStorage.__objects[key] = State(**value)
                    elif class_name == 'Amenity':
                        FileStorage.__objects[key] = Amenity(**value)
                    elif class_name == 'Review':
                        FileStorage.__objects[key] = Review(**value)
