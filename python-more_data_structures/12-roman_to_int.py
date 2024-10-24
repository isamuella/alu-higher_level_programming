#!/usr/bin/python3


def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    elif not roman_string:
        return 0
    else:

         roman_vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                       'C': 100, 'D': 500, 'M': 1000}
         result = 0
         prev_val = 0

         for char in reversed(roman_string):
             curr_val = roman_vals[char]

             if curr_val >= prev_val:
                result += curr_val
             else:
                result -= curr_val

             prev_val = curr_val
         return result
