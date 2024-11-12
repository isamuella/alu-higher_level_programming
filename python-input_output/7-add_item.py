#!/usr/bin/python3
"""
This script adds all arguments passed to it to a Python list
and saves the list to a JSON file.
    - Uses save_to_json_file from 5-save_to_json_file.py
    - Uses load_from_json_file from 6-load_from_json_file.py
    - Saves the list in add_item.json
"""


import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


filename = "add_item.json"
try:
    # Try to load existing items from the file
    items = load_from_json_file(filename)
except FileNotFoundError:
    # If the file doesn't exist, start with an empty list
    items = []
# Add new arguments to the list
items.extend(sys.argv[1:])
# Save the updated list back to the file
save_to_json_file(items, filename)
