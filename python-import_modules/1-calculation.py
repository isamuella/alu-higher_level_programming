#!/usr/bin/python3

from calculator_1 import add,sub,mul,div

if __name__ == "__main__":
    a = 10
    b = 5
    add = add(a, b)
    subtract = sub(a, b)
    multiply = mul(a, b)
    divide = div(a, b)
    print("{} + {} = {}".format(a, b, add))
    print("{} - {} = {}".format(a, b, subtract))
    print("{} * {} = {}".format(a, b, multiply))
    print("{} / {} = {}".format(a, b, divide))
