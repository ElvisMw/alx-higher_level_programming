#!/usr/bin/python3
"""class Rectangle that defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:
    """Class for the rectsngle"""

    def __init__(self, width=0, height=0):
        """Responsible for initializing a rectangle

        Args:
            width (int): This is the new rectangle's width.
            height (int): The is the rectangle's height
            """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
