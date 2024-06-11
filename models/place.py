#!/usr/bin/python3
"""Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that inherits from BaseModel.

    Attributes:
        city_id (str): The id of the city
        user_id (str): User that own the apartment
        description (str): description of apartment
        number_rooms (int): number of rooms in the apartment
        max_guest (int): number of guest that the apartment can acommodate
        price_by_night (int): rent amount per night
        latitude (float): The latitude of the apartment
        longititude (float): The longititude of the apartment
        amenity_ids (list): List of amenities.
        name (str): The name of the state.
    """

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
