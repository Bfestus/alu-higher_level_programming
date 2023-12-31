#!/usr/bin/python3
""" creating the empty class"""


class Rectangle:
    """defining rectange"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    """defining a getter, width"""
    @property
    def width(self):
        return self.__width
    """defining a setter, width"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    """defining a getter, height"""
    @property
    def height(self):
        return self.__height
    """defining a setter"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
