#!/usr/bin/python3
'''Creates an empty class called BaseGeometry
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
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

