#!/usr/bin/python3
"""User class module."""
from models.base_model import BaseModel

class User(BaseModel):
    """
    User class that inherits from BaseModel.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new User instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
        super().__init__(*args, **kwargs)
