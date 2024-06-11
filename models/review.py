#!/usr/bin/python3
"""Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.

    Attributes:
        place_id (str): The id of the place reviewed.
        user_id (str): The user's id that reviewed.
        text (str): User's comment.
    """

    place_id = ''
    user_id = ''
    text = ''
