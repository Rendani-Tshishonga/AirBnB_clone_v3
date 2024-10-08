#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Tablename of the states database abstraction"""
    __tablename__ = 'states'
    name  = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='delete')
