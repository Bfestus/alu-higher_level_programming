#!/usr/bin/python3
""" creating the empty class"""


class Rectangle:
    """ defining a rectangle """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    """ defining the getter"""    
    @property
    def width(self):
        return self.__width
    """defining the setter"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
    @property
    def height(self):
        return self.__height
    """defining the getter"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")