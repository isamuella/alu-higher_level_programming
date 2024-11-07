#!/usr/bin/python3
"""based on BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A child class"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
  
    def area(self):
        """For finding area"""
        return self.__width * self.__height

    def __str__(self):
         """for representing the string"""
         return f"[Rectangle] {self.__width}/{self.__height}"
