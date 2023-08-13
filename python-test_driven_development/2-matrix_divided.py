#!/usr/bin/python3
"""
    matrix division module
"""


def matrix_divided(matrix, div):
    """ Takes a matrix and divides the values by 'div'.

    Args:
        matrix (:obj:'list' of :obj:'list'): lists of lists of integers/floats.
        div (int or float): The divisor.
    """
    # Check if matrix is a list of lists of integers/floats
    if not (type(matrix) == list) or not all(type(row) == list for row in matrix) or \
       not all(type(num) in (int, float) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists)of integers/floats")

    # Check if each row of the matrix has the same size
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not (type(div) in (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
