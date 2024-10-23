#!/usr/bin/python3


#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Extract elements from the tuples, using 0 as a default for missing values
    a1, a2 = (tuple_a + (0, 0))[:2]  # Default to 0 if tuple_a has less than 2 elements
    b1, b2 = (tuple_b + (0, 0))[:2]  # Default to 0 if tuple_b has less than 2 elements

    # Return the sum of the corresponding elements as a new tuple
    return (a1 + b1, a2 + b2)
