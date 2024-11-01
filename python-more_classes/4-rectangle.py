#!/usr/bin/python3

"""Create an empty class Rectangle"""


class Rectangle:
    """Already created Rectangle class"""
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

    @height.setter
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

    def area(self):
        """Calculate the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """print the rectangle with character #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        return "\n".join("#" * self.__width for i in range(self.__height)i)

    def __repr__(self):
        """a string representation"""
        return f"Rectangle({self.__width}, {self.__height})"
