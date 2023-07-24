#!/usr/bin/python3
"""Define a class"""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new square."""
        self.size = size
    """defining the getter"""
    @property
    def size(self):
        """To get the size"""
        return self.__size
    """ defining the setter"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        return self.__size ** 2
    def my_print(self):
        if self.__size == 0:
            print()  # empty line 
        else:
            for i in range(self.__size):
                print("#" * self.__size)
