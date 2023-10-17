#!/usr/bin/python3
"""a class MyInt that inherits from int"""


class MyInt(int):
    """
    MyInt is a custom integer class that inherits from the int class.

    It has the == and != operators inverted.
    """

    def __eq__(self, value):
        """
        Custom implementation of the == operator.

        Args:
            value (int): The value to compare with.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return self.real != value

    def __ne__(self, value):
        """
        Custom implementation of the != operator.

        Args:
            value (int): The value to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return self.real == value
