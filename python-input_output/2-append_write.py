#!/usr/bin/python3
"""Append a string at the end of the text file"""


def append_write(filename="", text=""):
    """function to append"""
    with open(filename, mode="a", encoding="utf_8") as a_file:
        new_char_num = a_file.write(text)
        return new_char_num
