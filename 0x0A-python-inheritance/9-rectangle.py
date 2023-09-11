#!/usr/bin/python3
""" This is a class Rectangle that inherits from
BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Attributes:
        __width (int): The private width of the rectangle.
        __height (int): The private height of the rectangle.

    Example:
        r = Rectangle(3, 5)
        print(r)  # Output: [Rectangle] 3/5
        print(r.area())  # Output: 15
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle object with a given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string in the format "[Rectangle] <width>/<height>".
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
