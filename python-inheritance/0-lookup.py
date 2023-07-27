#!/usr/bin/python3
"""define a class """
def lookup(obj):
    """ returns the list of available attributes and methods of an object:
    we use dir()to get a list of attributs and methodes"""
    attribute_list = dir(obj)
    return attribute_list
