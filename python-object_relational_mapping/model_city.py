#!/usr/bin/python3

"""Defines a City model that inherits from
SQLAlchemy Base and links to the MySQL table cities"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """A city for a MySQL database.

    Attributes:
        id (str): The id of the city.
        name (sqlalchemy.Integer): The name of the city.
        state_id (sqlalchemy.String): The state id of the city.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
