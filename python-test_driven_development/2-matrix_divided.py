#!/usr/bin/python3
"""Module for math operation: division"""


def matrix_divided(matrix, div):
    """Function divides all elements given.

    Args:
        matrix: A list of lists contaning integers or floats
        div: The divisor

    Raises:
         TypeError: If matrix is not a list of lists.
         TypeError: If div is not a number (int or float).
         TypeError: If matrix is not of the same size.
         ZeroDivisionError: If div is 0.
         
    Returns:
         A new matrix with the division answer
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
