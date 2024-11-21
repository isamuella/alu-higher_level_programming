#!/usr/bin/python3
"""
Module for math operations
"""


def add_integer(a, b=98):
    """
    Function adds two numbwers
    Args:
        a: First number that has to be an integer or a float.
        b: Second number that has to be an integer or a float but has a default 98.

    Returns:
        The addition of integers 'a' and 'b'.

    Raises:
        TypeError: If 'a' or 'b' is not an integer or a float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int)and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
