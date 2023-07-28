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
    with open(my_obj, 'w') as file:
        """returns the JSON representation of an object"""
        json_represantation =  json.dump(my_obj, file)
        return json_represantation
    

