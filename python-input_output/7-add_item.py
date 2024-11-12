#!/usr/bin/python3
"""Script that adds all arguments to python list, and then save them to a file"""


import sys
from os import path
save_from_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if path.exists(filename):
    args = load_from_json_file(filename)
else:
    args = []

# Adds a new argument to the list
args.extend(sys.argv[1:])
# Saves the new list to the file
save_to_json_file(args, filename)
