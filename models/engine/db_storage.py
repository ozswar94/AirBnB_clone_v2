#!/usr/bin/python3
""" define DBStorage Class """
from os import getenv
from models.base_model import Base
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

class DBStorage:
    """ class DBStorage handle the MySQL DataBase """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}}/{}'.format(
        getenv("HBNB_MYSQL_USER"),
        getenv("HBNB_MYSQL_PWD"),
        getenv("HBNB_MYSQL_HOST"),
        gentenv("HBNB_MYSQL_DB"), pool_pre_ping=True))

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)


