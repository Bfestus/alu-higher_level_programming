#!/usr/bin/python3
"""
Module for Write_file method.
"""
def write_file(filename="", text=""):
    """
    Write a string to the text file
    """
    with open(filename, 'w', encoding="UTF-8") as file:
        """
        Writing the a string to  text file
        """
        text = file.write(filename)
        return text
