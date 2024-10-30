#!/usr/bin/python3


"""
To create a class to define a square with a private attribute called size and a method to calculate the area.
"""


class Square:
    """
    Class that defines a square and calculates are of the square.
    """
    def __init__(self, size=0):
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except Exception as e:
            raise e
        def area(self):
            self.area = area
            area_result = size * size
            print("{}" * "{}" = "{}".format(size, size, area_result))
