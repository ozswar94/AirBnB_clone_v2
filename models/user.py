#!/usr/bin/python3
""" class user module """
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """ class User that inherits from Base
        Attribute:
            email: string for email
            password: string for password
            first_name: string for first name
            last_name: string for last name
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    """
