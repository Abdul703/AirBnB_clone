#!/usr/bin/python3
"""
Base class for all subsequent classes.
This module defines the BaseModel class,
which serves as the base class for other models.
"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    The Base class for all models, providing common attributes and methods.
    """
    
    def __init__(self):
        """
        Initialize the base class with unique ID, and creation
        and update timestamps.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the instance.
        
        Returns:
            str: The string representation in the format
                '[<class name>] (<self.id>) <self.__dict__>'
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def to_dict(self):
        """Return a dictionary containing all keys/values of the instance.
        
        Returns:
            dict: A dictionary representation of the instance, with ISO formatted date strings and class name.
        """
        instance_dict = self.__dict__.copy()
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        instance_dict['__class__'] = self.__class__.__name__
        return instance_dict

    def save(self):
        """Update the `updated_at` attribute with the current datetime."""
        self.updated_at = datetime.now()
