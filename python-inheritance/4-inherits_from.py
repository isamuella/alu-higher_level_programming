#!/usr/bin/python3

"""If is directly or indirectly an instance"""


def inherits_from(obj, a_class):
    """Return True if not an instance"""
    return isinstance(obj, a_class) and type(obj) is not a_class
