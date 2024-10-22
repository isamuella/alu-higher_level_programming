#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":
    args = []
    for arg in argv[1:]:
        args.abs(int(arg))
        sum_args = sum(args)
        print("{}".format(sum_args))
