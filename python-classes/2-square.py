#!/usr/bin/python3


"""
To create a class to define a square with a private attribute called size.
"""


class Square:
    """
    Class that defines a square.
    """
    def __init__(self, size=0):
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            self.__size = size
        except Exception as e:
            print(e)
