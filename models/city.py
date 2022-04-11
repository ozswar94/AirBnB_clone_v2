#!/usr/bin/python3
""" class city definition """
from models.base_model import BaseModel


class City(BaseModel):
    """ class City that inherits from Base
        Attribute:
            state_id: State.id()
            name: name
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
