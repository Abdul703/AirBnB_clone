#!/usr/bin/python3
"""Base class for all subsequent classes"""
from datetime import datetime
from uuid import uuid4
import json


class BaseModel:
    """The Base class"""
    
    def __init__(self):
        """initialise the base class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """print the class info"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def to_dict(self):
        """deserialize class object"""
        d = self.__dict__
        d['created_at'] = d['created_at'].isoformat()
        d['updated_at'] = d['updated_at'].isoformat()
        d['__class__'] = self.__class__.__name__
        return d

    def save(self):
        """save the changes made to an object"""
        self.updated_at = datetime.now()
