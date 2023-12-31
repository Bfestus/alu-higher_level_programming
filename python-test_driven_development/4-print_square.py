#!/usr/bin/python3
""" Module for square
"""


def print_square(size):
    """ Function that prints a square using '#' based on `size`.

    Arguments:
        size (int): The size of one side of the square.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is not float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
