#!/usr/bin/python3

from calculator_1 import add,sub,mul,div

if __name__ == "__main__":
    a = 10
    b = 5
    sum = a + b
    print("{} + {}".format(a, b, sum))
    sub = a - b
    print("{} - {}".format(a, b, sub))
    mul = a * b
    print("{} * {}".format(a, b, mul))
    div = a / b
    print("{} / {}".format(a, b, div))
