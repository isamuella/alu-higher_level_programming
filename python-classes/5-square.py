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

    @size.setter
    def size(self, value):
        """
        Sets a private attribute for the square size.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the char #"""
        if size == 0:
            print("")
        else:
            for _ in range(self.size):
                print("{}".format("#" * self.size))
