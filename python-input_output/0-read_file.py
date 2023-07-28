#!/usr/bin/python3
"""
Module: file_reader
Description: A module to read and print the content of a text file.
"""


def read_file(filename=""):
    """
    Read and print the content of the specified text file.

    Parameters:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    if not filename:
        print("Error: No filename provided.")
        return
    
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
