#!/usr/bin/python3
"""This is a class BaseGeometry (based on 6-base_geometry.py)"""

class BaseGeometry:
    """
    A base class for geometry-related functionality.

    This class defines two public instance methods:
    - `area(self)`: Raises an Exception with the message "area() is
    not implemented" when called.
    - `integer_validator(self, name, value)`: Validates that
    a given value is an integer and greater than 0; otherwise, it
    raises appropriate exceptions.

    Example:
        bg = BaseGeometry()
        try:
            print(bg.area())  # Output: [Exception] area() is not
            implemented
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))

        try:
            bg.integer_validator("side_length", 5)
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
    """

    def area(self):
        """
        Raise an Exception with the message "area() is not
        implemented."

        Args:
            self: The instance of the class.

        Raises:
            Exception: Always raises an Exception with the
            specified message.

        Returns:
            None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that a given value is an integer and greater than 0.

        Args:
            self: The instance of the class.
            name (str): The name of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        Returns:
            None
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
