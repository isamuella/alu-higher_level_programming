#!/usr/bin/python3
"""
A first class Base
"""


class Base:
    """class Base to manage id attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the Base instance

        Args:
            id(int): An id instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_objects

    @classmethod
    def reset_nb_objects(cls):
        """Reset the private class attribute __nb_objects"""
        cls.__nb_objects = 0
