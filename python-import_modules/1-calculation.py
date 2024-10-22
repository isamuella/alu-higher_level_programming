#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    add_ans = add(a, b)
    sub_ans = sub(a, b)
    mul_ans = mul(a, b)
    div_ans = div(a, b)
    print("{} + {} = {}".format(a, b, add_ans))
    print("{} - {} = {}".format(a, b, sub_ans))
    print("{} * {} = {}".format(a, b, mul_ans))
    print("{} / {} = {}".format(a, b, div_ans))
