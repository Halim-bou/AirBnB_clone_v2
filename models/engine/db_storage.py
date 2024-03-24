#!/usr/bin/python3
""" db_storage Module"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from sqlalchemy import inspect
from os import environ
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """ Create an engine """
        mysql_user = environ.get('HBNB_MYSQL_USER')
        mysql_password = environ.get('HBNB_MYSQL_PWD')
        mysql_host = environ.get('HBNB_MYSQL_HOST')
        mysql_db = environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            mysql_user, mysql_password, mysql_host, mysql_db),
            pool_pre_ping=True)

        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def reload(self):
        """ Create a Session """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def new(self, obj):
        """ Add new inst into Session """
        attrs = obj.to_dict()
        cls = obj.__class__
        new_instance = cls()
        for key, value in attrs.items():
            if key == "__class__":
                continue
            setattr(new_instance, key, value)
        self.__session.add(new_instance)

    def save(self):
        """ Commit the changes into the data base """
        self.__session.commit()

    def all(self, cls=None):
        """ Return a dictionary of instances """
        classes = {
                "State": State,
                "City": City,
                "User": User,
                "Place": Place,
                "Review": Review,
                "Amenity": Amenity,
                }
        dictionary = {}
        if cls:
            #inst_class = classes[cls.__name__]
            #if isinstance(inst_class, str):
               # inst_class = classes[cls]
            if isinstance(cls, str):
                inst_class = classes.get(cls)
            else:
                inst_class = cls
            for inst in self.__session.query(inst_class).all():
                key = f"{inst_class.__name__}.{inst.id}"
                dictionary[key] = inst
        else:
            for cls in classes.values():
                for inst in self.__session.query(cls).all():
                    key = f"{cls.__name__}.{inst.id}"
                    dictionary[key] = inst
        return dictionary

    def delete(self, obj=None):
        """ Deletes an instance from a database """
        classes = {
            "states": State,
            "cities": City,
            "users": User,
            "places": Place,
            "Review": Review,
            "Amenity": Amenity,
        }
        if not obj:
            return

        table = Base.metadata.tables[obj.__tablename__]
        cls = classes[str(table)]
        wanted_row = self.__session.query(cls)\
            .where(cls.id == obj.id).one_or_none()
        if not wanted_row:
            return

        self.__session.delete(wanted_row)
        self.__session.commit()

    def close(self):
        """
        calling  close() on the class Session
        """
        self.__session.close()
