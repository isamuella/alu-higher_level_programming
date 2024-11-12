#!/usr/bin/python3
"""Write an object to text file"""

import json


def save_to_json_file(my_obj, filename):
    """functioon to write an object to a textfile using json"""
    with open(filename, mode="w", encoding="utf-8") as a_file:
        json.dump(my_obj, a_file)
