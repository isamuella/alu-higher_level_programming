#!/usr/bin/python3
"""The JSON representation of an object"""

import json


def to_json_string(my_obj):
    """function to return the json of an object"""
    new_str = json.dumps(my_obj)
    return new_str
