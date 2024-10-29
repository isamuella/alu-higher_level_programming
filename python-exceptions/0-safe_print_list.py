#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for s in range(x):
            print(my_list[s], end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
    
