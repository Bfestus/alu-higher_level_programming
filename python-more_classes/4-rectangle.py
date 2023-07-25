#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Class representing a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The width value to set.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The height value to set.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the Rectangle.

        Returns:
            str: The string representation of the Rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return "\n".join(["#" * self.width] * self.height)
   
    def __repr__(self):
        """Return a string representation of the Rectangle.

        Returns:
            str: The string representation of the Rectangle.
        """
        return f"({self.width}, {self.height})"
