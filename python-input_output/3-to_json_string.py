#!/usr/bin/python3
"""
Module to_json_string method.
"""


import json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string)
    firstly we have to serialize object string
    """
    return (json.dumps(my_obj))
