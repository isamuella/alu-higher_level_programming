#!/usr/bin/python3
number = 3.14159

try:
    number+1
print(f"Float: {number:.2f}")
except:
    print("ValueError: Unknown format code 'f' for object of type 'str'")
