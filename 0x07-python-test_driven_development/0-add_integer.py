#!/usr/bin/python3
"""This function add two numbers"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number for addition.
        b (int or float, optional): The second number
        for addition. Defaulted to 98.

    Returns:
        int: The sum of the two input numbers, cast to an integer.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.
    """
    if a is None:
        raise ValueError("a cannot be None")
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
