#!/usr/bin/python3
"""The JSON representation of an object"""


def to_json_string(my_obj):
    """function to return the json of an object"""
    new_str = json.dump(my_obj)
    print(new_str)
