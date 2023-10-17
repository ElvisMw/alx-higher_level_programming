#!/usr/bin/python3
"""This function returns the dictionary description with
simple data structure."""


def class_to_json(obj):
    """
    Convert a class instance to a serializable dictionary for
    JSON serialization.

    This function takes an instance of a class and returns a
    dictionary representation of its attributes, making sure that
    all attributes of the class are serializable
    (e.g., list, dictionary, string, integer, and boolean).

    Parameters:
    - obj (object): An instance of a class to be converted to
    a serializable dictionary.

    Returns:
    - dict: A dictionary representation of the object's attributes.

    Note:
    - This function assumes that all attributes of the
    class are serializable.

    Example:
    >>> class MyClass:
    ...     def __init__(self, name):
    ...         self.name = name
    ...         self.number = 0
    ...
    ...     def __str__(self):
    ...         return "[MyClass] {} - {:d}".format(self.name, self.number)
    ...
    >>> m = MyClass("John")
    >>> m.number = 89
    >>> mj = class_to_json(m)
    >>> print(type(mj))
    <class 'dict'>
    >>> print(mj)
    {'name': 'John', 'number': 89}
    """
    return obj.__dict__
