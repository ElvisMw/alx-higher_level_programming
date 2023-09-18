#!/usr/bin/python3
"""Represents a class of square which is a specail rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class represents a square, which is a special case of a rectangle.
    It inherits properties and methods from the Rectangle class.

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): The unique identifier of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square's sides.
            x (int): The x-coordinate of the square's position (default is 0).
            y (int): The y-coordinate of the square's position (default is 0).
            id (int): The unique identifier of the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        int: The size of the square's sides. Can be accessed and modified
        using this property, which is equivalent to changing the width and height.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square's sides, updating both width and height.

        Args:
            value (int): The new size of the square's sides.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the square's attributes based on positional arguments or keyword arguments.

        Args:
            *args: Positional arguments to update the square's attributes.
            **kwargs: Keyword arguments to update the square's attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for e_m, b_k in kwargs.items():
                if e_m == "id":
                    if b_k is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = b_k
                elif e_m == "size":
                    self.size = b_k
                elif e_m == "x":
                    self.x = b_k
                elif e_m == "y":
                    self.y = b_k

    def to_dictionary(self):
        """
        Return a dictionary representation of the square's attributes.

        Returns:
            dict: A dictionary containing the square's id, size, x, and y.
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string describing the square's type, id, position, and size.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
