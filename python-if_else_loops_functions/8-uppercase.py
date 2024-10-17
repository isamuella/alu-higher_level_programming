#!/usr/bin/python3


def uppercase(str):
    a = ord('a')
    b = ord('z')
    for char in str:
        if a <= ord(char) <= b:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()
