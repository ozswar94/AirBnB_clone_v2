#!/usr/bin/python3
""" module for class base and derived class """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class that inherits from Base
        Attribute:
            name: string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
