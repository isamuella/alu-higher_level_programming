#!/usr/bin/python3
""" Based on Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A child class"""
    def __init__(self, size):
        self.integer_validator = ("size", size)
        self.size = size

    def area(self):
        """For finding the area"""
        return self.size * self.size
