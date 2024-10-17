#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(your number, "is positive")
elif number < 0:
    print(your number, "is negative")
elif number == 0:
    print(your number, "is zero")
else:
    print("Error:something is wrong")
