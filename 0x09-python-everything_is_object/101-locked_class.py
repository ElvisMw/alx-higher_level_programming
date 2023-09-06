#!/usr/bin/python3
"""This defines a locked class"""


class LockedClass:
    """
    The LockedClass restricts the creation of new instance attributes.

    Attributes:
        __slots__ (tuple of str): A tuple specifying
        the allowed instance attributes.
    """
    __slots__ = ('first_name',)
