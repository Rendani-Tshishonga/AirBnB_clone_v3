#!/usr/bin/python3
"""
Import the necessary libraries
"""
import os
from sqlalchemy import create_engine, MetaData
from models.base_model import user, place, amenity, review, state
from sqlalchemy.orm import scoped_session, sessionmaker

class DBStorage():
    cls_dict = {
            BaseModel: base_model.BaseModel,
            User: user.User,
            Place: place.Place,
            Amenity: amenity.Amenity,
            Review: review.Review,
            State: state.State
            }
    
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
                    pool_pre_ping=True))
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

    def get(self, cls, id):
        """A method to retrieve an object"""
        object_class = self.all()
        for obj in object_class.values():
            if id == str(obj.id):
                return obj
            else:
                return None

    def count(self, cls=None):
        """A method to count objects in storage"""
        if cls is not None:
            return len(self.all(cls))
        else:
            return len(self.all())
