#!/usr/bin/python3
"""This is a class BaseGeometry (based on 5-base_geometry.py)"""

class BaseGeometry:
    """
    A base class for geometry-related functionality.

    This class defines a public instance method `area(self)` that
    raises an Exception with the message "area() is
    not implemented" when called.

    Example:
        bg = BaseGeometry()
        try:
            print(bg.area())  # Output: [Exception] area() is
            not implemented
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
    """
    def area(self):
        """
        Raise an Exception with the message "area() is not implemented."

        Args:
            self: The instance of the class.

        Raises:
            Exception: Always raises an Exception with
            the specified message.

        Returns:
            None
        """
        raise Exception("area() is not implemented")
