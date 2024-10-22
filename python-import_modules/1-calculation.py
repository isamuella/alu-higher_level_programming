#!/usr/bin/python3

from calculator_1 import add,sub,mul,div

if __name__ == "__main__":
    a = 10
    b = 5
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b
    print("{} + {}".format(a, b, sum))
    print("{} - {}".format(a, b, sub))
    print("{} * {}".format(a, b, mul))
    print("{} / {}".format(a, b, div))
