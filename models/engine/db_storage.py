#!/usr/bin/python3
""" define DBStorage Class """
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from sqlalchemy.orm import Session, sessionmaker, scoped_session
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

    def all(self, cls=None):
        """ return all table or all table by cls"""
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(elem.__name__, elem.id)
                dic[key] = elem
        else:
            for classe in [User, State, City, Amenity, Place, Review]:
                query = self.__session.query(classe)
                for elem in query:
                    key - "{}.{}".format(type(elem).__name__, elem.id)
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
