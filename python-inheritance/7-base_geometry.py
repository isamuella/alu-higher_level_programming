#!/usr/bin/python3

"""based on BaseGeometry"""


class BaseGeometry:
    """a class BaseGeometry"""

    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if not type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
