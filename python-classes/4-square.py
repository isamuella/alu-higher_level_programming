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
        return self.__size

    @propertysetter
    def size(self, value):
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        except Exception as e:
            raise e

    def area(self):
        return self.__size ** 2
