#!/usr/bin/python3
""" module for class base and derived class """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.city import City
from sqlalchemy import ForeignKey


class State(BaseModel, Base):
    """ State class that inherits from Base
        Attribute:
            name: string
    """
    __tablename__ = "states"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete', backref="state")

    @property
    def cities(self):
        list_city = []
        for city in models.storage.all(City).values():
            if self.id == city.state_id:
                list_city.append(city)
        return list_city
