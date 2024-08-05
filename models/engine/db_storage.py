#!/usr/bin/python3
"""
Import the necessary libraries
"""

import os
from sqlalchemy import create_engine, MetaData
from models.base_model import Base
from sqlalchemy.orm import scoped_session, sessionmaker

class DBStorage():
    """Private class attributes"""
    __engine = None
    __session = None

    def __init__(self):
        """Create the engine self.__engine"""
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                    os.environ.get('HBNB_MYSQL_USER'),
                    os.environ.get('HBNB_MYSQL_PWD'),
                    os.environ.get('HBNB_MYSQL_HOST'),
                    os.environ.get('HBNB_MYSQL_DB'),
                    pool_pre_ping=True)
        if os.environ.get['HBNB_ENV'] == 'test':
            Base.metadata.drop_all(self.__engine)

    def new(self, obj):
        """Add object to current database object"""
        return self.__engine.add(obj)
    def save(self):
        """Commmit all changes to the current database session"""
        return self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj is not None:
            return self.__session.delete(obj)
    def reload(self):
        """Creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        """Create the current database session"""
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False))
