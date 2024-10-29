#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            # Attempt division if elements exist in both lists
            div = my_list_1[i] / my_list_2[i]
        except IndexError:
            # Handle cases where lists are shorter than list_length
            print("out of range")
            div = 0
        except TypeError:
            # Handle cases where elements are not integers or floats
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            # Handle division by zero errors
            print("division by 0")
            div = 0
        finally:
            # Append the result (either division result or 0 for errors)
            result_list.append(div)
    return result_list

