#!/usr/bin/python3
"""
    Module containing add_integer function.
    The function returns two integers.
    5 line module comment.
"""
def add_integer(a, b=98):
     """ Add two integers and returns the result.
    Args:
        a (int): The first integer.
        b (int): The secodn integer.
    """
    if not isinstance(a(int, float)) or not isinstance(b(int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
        
