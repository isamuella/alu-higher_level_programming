#!/usr/bin/python3


"""Creates an empty class Rectangle"""


class Rectangle:
    """Already created an empty class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    @property
    def width(self):
        """created a getter method for the __width attribute"""
        return self.__width

    @property
    def height(self):
        """created a getter method for the __height attribute"""
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets a private attribute for the Rectangle width.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.seter
    def height(self, value):
        """
        Sets a private attribute for the Rectangle height.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
