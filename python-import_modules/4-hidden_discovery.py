#!/usr/bin/python3

if __name__ == "__main__":
import hidden_4

 i = dir(hidden_4)
 new_i = [for name in i if not name.starting('__')]

 for name in new_i:
     print(name)
