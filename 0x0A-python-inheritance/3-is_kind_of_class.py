#!/usr/bin/python3
""" This function that returns True if the object is an instance of, or
if the object is an instance of a class that inherited from,
the specified class ; otherwise False"""


def is_kind_of_class(obj, a_class):
    """
    Check if the given object is an instance of, or inherits from,
    the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the
        specified class or inherits from it; otherwise, False.

    Example:
        a = 1
        if is_kind_of_class(a, int):
            print("{} comes from {}".format(a, int.__name__))
            # Output: "1 comes from int"
        if is_kind_of_class(a, float):
            print("{} comes from {}".format(a, float.__name__))
        if is_kind_of_class(a, object):
            print("{} comes from {}".format(a, object.__name__))
            # Output: "1 comes from object"
    """
    if isinstance(obj, a_class):
        return True
    return False
