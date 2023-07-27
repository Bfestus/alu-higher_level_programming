#!/usr/bin/python3
"""Contain the Mylist class."""

class Mylist(list):
    """A subclass of list that provides additional methods."""
    def __init__(self):
            """initializing the object"""
        super().__init__()

    def print_sorted(self):
        """Prints the elements of the list in sorted order."""
        sorted_list = sorted(self)
        print(sorted_list)
