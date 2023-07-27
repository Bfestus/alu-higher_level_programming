#!/usr/bin/python3
'''New class rectangle inherits from BaseGeometry
'''
class BaseGeometry:
    '''Class BaseGeometry
    '''
    def area(self):
        '''Calculates area
        '''
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        '''Validates value
        '''
        if type(value) != int:
            raise TypeError("<width> must be an integer")
        if value <= 0:
            raise ValueError("<height> must be greater than 0")


class Rectangle(BaseGeometry):
    '''New Rectangle class inherits from BaseGeometry, and represents a
    rectangle'''
    def __init__(self, width, height):
        '''Initializes new Rectangle obj
        '''
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
