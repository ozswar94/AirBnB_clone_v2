#!/usr/bin/python3
""" class user module """
from models.base_model import BaseModel


class User(BaseModel):
    """ class User that inherits from Base
        Attribute:
            email: string for email
            password: string for password
            first_name: string for first name
            last_name: string for last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
