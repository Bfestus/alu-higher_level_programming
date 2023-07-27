#!/usr/bin/python3
""" contain the Mylist class"""


class Mylist(list):
    """a subclass of list"""
    def print_sorted(self):
        """ prints sorted lists"""
        sort_list = sorted(self)
        print(sort_list)
