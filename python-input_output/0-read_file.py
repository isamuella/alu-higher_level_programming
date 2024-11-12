#!/usr/bin/python3
"""Reading a text file"""

def read_file(filename=""):
    """function to read the file filename"""
    with open(filename, mode="r", encoding="utf-8") as a_file:
        print(a_file.read())
