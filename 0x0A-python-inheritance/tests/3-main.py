#!/usr/bin/python3
is_same_class = __import__('2-is_same_class').is_same_class

a = 1
"""
Create an integer variable 'a' with the value 1.

Example:
    a = 1
"""

if is_same_class(a, int):
    """
    Check if 'a' is an instance of the 'int' class.

    Example:
        Output (if 'a' is an instance of 'int'):
        1 is an instance of the class int
    """
    print("{} is an instance of the class {}".format(a, int.__name__))

if is_same_class(a, float):
    """
    Check if 'a' is an instance of the 'float' class.

    Example:
        Output (if 'a' is not an instance of 'float'):
        (no output)
    """
    print("{} is an instance of the class {}".format(a, float.__name__))

if is_same_class(a, object):
    """
    Check if 'a' is an instance of the 'object' class.

    Example:
        Output (if 'a' is an instance of 'object'):
        1 is an instance of the class object
    """
    print("{} is an instance of the class {}".format(a, object.__name__))
