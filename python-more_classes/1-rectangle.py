#!/usr/bin/python3


"""Creates an empty class Rectangle"""


class Rectangle:
    """Already created an empty class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
@property
def width(self):
    return self.__width

@property
def height(self):
    return self.__height

@width.setter
def width(self, value):
    if isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self.__width = value

@height.seter
def height(self, value):
    if isinstance(value, int):
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self.__height = value
