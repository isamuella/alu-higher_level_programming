#!/usr/bin/python3
"""return an object by JSON string"""

import json


def from_json_string(my_str):
    """function to return an object represented by a json string"""
    new_obj = json.loads(my_str)
    return new_obj
