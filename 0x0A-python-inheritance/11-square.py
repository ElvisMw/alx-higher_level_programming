#!/usr/bin/python3
""" This is a class representing a square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.

    Args:
        size (int): The size of the square.

    Attributes:
        __size (int): The private size of the square.

    Example:
        s = Square(13)
        print(s)  # Output: [Square] 13/13
        print(s.area())  # Output: 169
    """

    def __init__(self, size):
        """
        Initialize a Square object with a given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
