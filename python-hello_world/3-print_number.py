#!/usr/bin/python3
number = 98
try:
    number+1
    print(f"{number} Battery street")
except ValueError:
    print("Unknown format code 'd' for object of type 'str')
