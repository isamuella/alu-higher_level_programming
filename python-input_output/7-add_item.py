#!/usr/bin/python3
"""Script that adds all arguments to python list, and then save them to a file"""


import sys
from os import path
from 5-save_to_json_file import save_to_json_file
"""Uses save_to_json_file from 5-save_to_json_file"""
from 6-load_from_json_file import load_from_json_file
"""Uses load_from_json_file from 6-load_from_json_file"""

filename = "add_item.json"
try:
    args = load_from_json_file(filename)
except FileNotFoundError:
    args = []
# Adds a new argument to the list
args.extend(sys.argv[1:])
# Saves the new list to the file
save_to_json_file(args, filename)
