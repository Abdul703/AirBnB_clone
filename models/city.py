#!/usr/bin/python3
"""City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.

    Attributes:
        name (str): The name of the state.
        state_id (str): The id of the city's state
    """

    name = ''
    state_id = ''
