#!/usr/bin/python3
"""Appends the given text to the specified file"""


def append_write(filename="", text=""):
    """
    Appends the given text to the specified file.

    Parameters:
    - filename (str): The name of the file to which the
    text will be appended.
    - text (str): The text to be appended to the file.

    Returns:
    - int: The number of characters written to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
