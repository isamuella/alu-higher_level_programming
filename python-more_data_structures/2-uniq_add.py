#!/usr/bin/python3


def uniq_add(my_list=[]):
    return reduce(lambda x, y: x + y, set(my_list))
