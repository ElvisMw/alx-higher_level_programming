#!/usr/bin/python3
inherits_from = __import__('4-inherits_from').inherits_from

a = True
"""
Create a Boolean variable 'a' with the value True.

Example:
    a = True
"""

if inherits_from(a, int):
    """
    Check if 'a' is an instance of a class that inherits from 'int'.

    Example:
        Output (if 'a' is an instance of a class tht inherits from 'int'):
        True inherited from class int
    """
    print("{} inherited from class {}".format(a, int.__name__))

if inherits_from(a, bool):
    """
    Check if 'a' is an instance of a class that inherits from 'bool'.

    Example:
        Output (since 'bool' is a built-in class and 'a' is of type bool):
        True inherited from class bool
    """
    print("{} inherited from class {}".format(a, bool.__name__))

if inherits_from(a, object):
    """
    Check if 'a' is an instance of a class that inherits from 'object'.

    Example:
        Output (since 'bool' is a subclass of 'object'):
        True inherited from class object
    """
    print("{} inherited from class {}".format(a, object.__name__))
