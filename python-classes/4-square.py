#!/usr/bin/python3


"""
To create a class to define a square with a private attribute called size.
"""


class Square:
    """
    Class that defines a square.
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """creates a getter method for the __size attribute"""
        return self.__size

    @property.setter
    """
    Sets the square size.

    raises:
        ValueError: if value is less than 0.
        TypeError: if value is not an integer.
    """
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
