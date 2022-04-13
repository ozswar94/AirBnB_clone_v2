#!/usr/bin/python3
""" module for class base and derived class """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class that inherits from Base
        Attribute:
            name: string
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    city = relationship("City", backref="state", cascade="delete")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        list_city = []
        for city in models.storage.all(City).values():
            if self.id == city.state_id:
                list_city.append(city)
        return list_city
