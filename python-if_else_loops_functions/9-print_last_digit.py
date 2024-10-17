#!/usr/bin/python3


def print_last_digit(number):
    try:
        last_digit = abs(int(number)) % 10
        print(last_digit, end="")
        return last_digit
    except ValueError:
        return "Traceback (most recent call last):"
