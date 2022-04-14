#!/usr/bin/python3
""" class place definition """
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class Place(BaseModel, Base):
    """ class Place that inherits from Base
        Attribute:
            city_id: City.id()
            user_id: User.id()
            name: name (string)
            description: description of Place
            number_rooms: int number of rooms
            number_bathrooms: int number of bathrooms
            max_guest: int max guest
            price_by_night: price
            latitude: latitude (float)
            longitude: longitude (float)
            amenity_ids: Amenity.id()
            """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
