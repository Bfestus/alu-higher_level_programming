#!/usr/bin/python3
import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_arguments_to_list(my_list, arguments):
    """
    Add command-line arguments to the given list.

    Parameters:
        my_list (list): The list to which the arguments will be added.
        arguments (list): A list of command-line arguments.

    Returns:
        list: The updated list with the added arguments.
    """
    my_list.extend(arguments)
    return my_list
