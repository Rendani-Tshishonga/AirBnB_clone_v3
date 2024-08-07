#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """Tablename of the states database abstraction"""
    __tablename__ = 'states'
    name  = Column(String(128), nullable=False)
