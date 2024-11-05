#!/usr/bin/python3

"""Checking if object is exactly an instance of a specified class"""


def is_same_class(obj, a_class):
    """Returns true if object is exactly an instance of a specified class"""
    return type(obj) is a_class
