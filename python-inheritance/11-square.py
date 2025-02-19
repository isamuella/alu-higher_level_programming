#!/usr/bin/python3
"""Based on Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A child class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """For representing the string"""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
