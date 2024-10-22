#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    arguments = []
    for arg in argv[1:]:
        arguments.append(int(arg))
    sum_arg = sum(arguments)
    print("{}".format(sum_arg))
