#!/usr/bin/python3
"""
Module for read_file method.
"""


def read_file(filename=""):
    """
    Reads text file and prints to STDOUT
    """
    with open(filename, 'r', encoding="UTF-8") as file:
        """
        reading the contend
        """
        content = file.read()
        print(content)
