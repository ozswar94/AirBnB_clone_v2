#!/usr/bin/python3
""" class city definition """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(BaseModel, Base):
    """ class City that inherits from Base
        Attribute:
            state_id: State.id()
            name: name
    """
    __tablename__ = "cities"
    state_id = Column(String(60), nullable=False, ForeignKey('states.id'))
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
