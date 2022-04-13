#!/usr/bin/python3
""" class city definition """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ class City that inherits from Base
        Attribute:
            state_id: State.id()
            name: name
    """
    __tablename__ = "cities"

    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    """

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    else:
        state_id = ""
        name = ""
