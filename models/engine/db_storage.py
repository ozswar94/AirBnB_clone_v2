#!/usr/bin/python3
""" define DBStorage Class """
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from sqlalchemy.orm import Session, sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.engine.url import URL


class DBStorage:
    """ class DBStorage handle the MySQL DataBase """
    __engine = None
    __session = None

    def __init__(self):

        mySQL_u = getenv("HBNB_MYSQL_USER")
        mySQL_p = getenv("HBNB_MYSQL_PWD")
        dbHost = getenv("HBNB_MYSQL_HOST")
        dbName = getenv("HBNB_MYSQL_DB")

        url = {'drivername': 'mysql+mysqldb', 'host': dbHost,
               'username': mySQL_u, 'password': mySQL_p, 'database': dbName}

        self.__engine = create_engine(URL(**url), pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ return all table or all table by cls"""
        dic = {}
        obj = []
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            obj = self.__session.query(cls)
        else:
            list_cls = [State, City, User]
            for item in list_cls:
                obj.extend(self.__session.query(item).all())
        for elem in obj:
            key = "{}.{}".format(type(elem).__name__, elem.id)
            dic[key] = elem
        return dic

    def new(self, obj):
        """ add new obj in table"""
        self.__session.add(obj)

    def save(self):
        """ save on DB """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from DB """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """  """
        Base.metadata.create_all(self.__engine)
        """Session Factory"""
        sf = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sf)
        self.__session = Session()
