#!/usr/bin/python3
"""
load_from_json_file method.
"""


import json


def load_from_json_file(filename):
    """
     creates an Object from a “JSON file”
    """
    with open(filename, "r") as file:
	created = json.loads(file)
        return created

