#!/usr/bin/python3
""" This function returns the list of available attributes and methods of an object"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to look up.

    Returns:
        A list of strings representing the attributes and methods of the object.
    """
    return dir(obj)
