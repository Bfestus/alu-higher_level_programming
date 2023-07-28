#!/usr/bin/python3
"""
Module for append_write method.
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file
    """
    with open(filename, 'a', encoding="UTF-8") as file:
        """
        appending the content
        """
        to_append = file.write(text)
        return to_append
