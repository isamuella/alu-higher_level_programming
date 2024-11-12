#!/usr/bin/python3
"""Add all arguments to python list"""


import sys

from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"
try:
    args = load_from_json_file(filename)
except FileNotFoundError:
    args = []

args.extend(sys.argv[1:])
save_to_json_file(args, filename)
