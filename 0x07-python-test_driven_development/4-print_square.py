#!/usr/bin/python3
""" Now this function prints a square with the charcter #"""


def print_square(size):
    """
    Prints a square using the character #.

    Args:
        size (int): Represents the size length of the square.

    Raises:
        TypeError: If `size` is not an integer or is a float.
        ValueError: If `size` is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("# (Empty line)")
    else:
        for _ in range(size):
            print("#" * size)
