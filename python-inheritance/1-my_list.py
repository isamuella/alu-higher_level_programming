#!/usr/bin/python3

"""A class MyList that inherits from list."""


class MyList(list):
    """The child class MyList that inheerits from list"""
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
