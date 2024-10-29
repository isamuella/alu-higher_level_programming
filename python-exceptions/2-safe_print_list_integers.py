#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for item in range(int(x)):
            if isinstance(item, int)
        print("{:d}".format(item), end="")
        break
    except IndexError:
        return my_list
