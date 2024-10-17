#!/usr/bin/python3


def islower(c):
    asci = ord(c)
    if 97 <= asci <= 122:
        return True
    elif 65 <= asci <= 90:
        return False
    else:
        return "not an ASCII"
