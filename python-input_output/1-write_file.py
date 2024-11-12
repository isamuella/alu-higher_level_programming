#!/usr/bin/python3
"""Write a string to a text file"""


def write_file(filename="", text=""):
    """function contaning the filename"""
    with open(filename, mode="w", encoding="utf_8") as a_file:
        num_char = a_file.write(text)
        return num_char
