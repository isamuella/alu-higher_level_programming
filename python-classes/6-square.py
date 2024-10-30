#!/usr/bin/python3


"""
To create a class to define a square with a private attribute called size.
"""


class Square:
    """
    Class that defines a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """creates a getter method for the __size attribute"""
        return self._size

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
        self._size = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(x, int)
            and x >=0 for x in value)): 
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """Calculate the area of the square."""
        return self._size ** 2

    def my_print(self):
        """prints in stdout the square with the char #"""
        if self.size == 0:
            print()
            return
        print("\n" * self.position[1], end="")
        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
