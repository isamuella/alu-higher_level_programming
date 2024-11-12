#!/usr/bin/python3
"""Create an object from json file"""

import json


def load_from_json_file(filename):
    """function to create an bject from json file"""
    with open(filename, mode="r", encoding="utf-8") as a_file:
        json.load(a_file)
