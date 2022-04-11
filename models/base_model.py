#!/usr/bin/python3
""" define BaseModel class """


import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ The BaseModel class """
    def __init__(self, *args, **kwargs):
        """ constructor of instance BaseModel """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        format_time = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    setattr(self, k, datetime.strptime(v, format_time))
                else:
                    if k != "__class__":
                        setattr(self, k, v)
        else:
            models.storage.new(self)

    def __str__(self):
        """ return string representation of object BaseModel"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """ save object in json file """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ return a object Base model in dict """
        dict = self.__dict__.copy()
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        dict["__class__"] = self.__class__.__name__
        return dict
