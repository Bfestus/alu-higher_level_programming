#!/usr/bin/python3
""" creating a class square."""


class Square:
    """initializing the class"""
    def __init__(self, size=0):
        """creating the exceptions"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        """ creating the instance attribute size"""
        self.__size = size
    """creating public instance method are """
    def area(self):
        """returning the square of size"""
        return self.__size ** 2
