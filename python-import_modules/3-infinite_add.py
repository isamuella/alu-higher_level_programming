#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":
    sum_args = sum(int(args) for args in argv[1:])
    print("{}".format(sum_args))
