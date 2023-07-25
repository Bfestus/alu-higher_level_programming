#!/usr/bin/python3
"""defining class rectangle"""


class Rectangle:
    """A class representing a Rectangle."""

    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle with optional width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
              The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.

        Returns:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.
             The height value to set.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle."""
 	if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)
    def __str__(self):
        """Return a string representation of the Rectangle,
        displaying it as a rectangle of '#' characters."""
        if self.width == 0 or self.height == 0:
            return("")
        else:
            for i in self.__width:
                print("#" * self.__width)
