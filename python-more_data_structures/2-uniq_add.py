#!/usr/bin/python3


def uniq_add(my_list=[]):
    total = reduce(lambda x,y: x+y, my_list)
    print(total)
