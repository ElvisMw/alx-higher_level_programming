#!/usr/bin/python3
""" A class representing a rectangle, inheriting from BaseGeometry"""


class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
        print(r)  # Output: <8-rectangle.Rectangle
        object at 0x7f6f488f7eb8>
        print(dir(r))  # Output: List of available attributes and
        methods

        try:
            print("Rectangle: {} - {}".format(r.__width, r.__height))
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))  # Output:
            [AttributeError] 'Rectangle' object has no attribute '__width'

        try:
            r2 = Rectangle(4, True)
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))  # Output:
            [TypeError] height must be an integer
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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
