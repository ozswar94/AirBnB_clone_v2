#!/usr/bin/python3
""" class Amenity definition """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ class Amenity that inherits from Base
        Attribute:
            name: name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
