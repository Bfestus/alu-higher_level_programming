#!/usr/bin/python3
"""
This module contains the function is_same_class
"""


def inherits_from(obj, a_class):
    """if the object is an instance of a class that inherited 
    (directly or indirectly) from the specified class """
    return isinstance(obj, object) and issubclass(type(obj), a_class) and type(obj) != a_class
