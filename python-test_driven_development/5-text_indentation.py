#!/usr/bin/python3
"""
Prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """a function that prints a text with 2 new lines after
     each of these characters: . ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char inn ".:?":
            print(result.strip())
            print()
            result = ""
    if result.strip():
        print(result.strip(), end="")
