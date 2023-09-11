#!/usr/bin/python3
""" This function returns True if the object is an instance of a
class that inherited (directly or indirectly) from the specified
class ; otherwise False"""

def inherits_from(obj, a_class):
    """
    Check if the given object is an instance of a class that
    inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a class that
        inherited from the specified class; otherwise, False.

    Example:
        a = True
        if inherits_from(a, int):
            print("{} inherited from class {}".format(a, int.__name__))
            # Output: "True inherited from class int"
        if inherits_from(a, bool):
            print("{} inherited from class {}".format(a, bool.__name__))
        if inherits_from(a, object):
            print("{} inherited from class {}".format(a, object.__name__))
            # Output: "True inherited from class object"
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
