#!/usr/bin/python3
"""
Module from_json_string method.
"""


import json


def from_json_string(my_str):
    """
    returns an object (Python data structure) represented by a JSON string
    firstly we have to serialize object string
    """
    return (json.loads(my_str))
