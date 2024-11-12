#!/usr/bin/python3
"""Write an object to text file"""

import json


def save_to_json_file(my_obj, filename):
    """functioon to write an object to a textfile usin json"""
    with open(filename, mode="w" encoding="utf_8")as a_file:
        json.dumps(my_obj, a_file)
