#!/usr/bin/python3


"""
This code create an empty class.
"""


class Square:
    """
    A class to represent a square.
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @property.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
