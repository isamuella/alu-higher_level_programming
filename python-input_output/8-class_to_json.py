#!/usr/bin/python3
"""Returns the dictionary description with a simple data structure for json"""


def class_to_json(obj):
    """function that returns dictionaty description"""
    return obj.__dict__
