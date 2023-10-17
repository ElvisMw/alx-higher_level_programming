#!/usr/bin/python3
""" This function returns True if the
object is exactly an instance of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """
    Check if the given object is really an instance of the specified class

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the
        specified class; otherwise, False

    Example:
        a = 1
        if is_same_class(a, int):
            print("{} is an instance of the
            class {}".format(a, int.__name__))  # Output: "1 is an
            instance of the class int"
        if is_same_class(a, float):
            print("{} is an instance of the
            class {}".format(a, float.__name__))
        if is_same_class(a, object):
            print("{} is an instance of the
            class {}".format(a, object.__name__))
    """
    if type(obj) == a_class:
        return True
    return False
