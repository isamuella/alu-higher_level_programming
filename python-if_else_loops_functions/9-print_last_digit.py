#!/usr/bin/python3


def print_last_digit(number):
    try:
        number = int(number)*1
        last_digit = str(number)[-1]
        print("{}".format(last_digit), end="")
        return last_digit
    except:
        return "Traceback:(most recent call last)"
