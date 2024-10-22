#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    i = dir(hidden_4)
    new_i = [name for name in i if not name.startswith('__')]

    for name in sorted(new_i):
        print(name)
