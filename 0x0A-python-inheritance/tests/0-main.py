#!/usr/bin/python3
lookup = __import__('0-lookup').lookup


class MyClass1(object):
    pass
    """
    A simple class for testing the 'lookup' function.

    Example:
        print(lookup(MyClass1))  # Output: A dictionary containing
        the attributes and methods of MyClass1.
    """
    pass


class MyClass2(object):
    """
    Another class for testing the 'lookup' function, with
    attributes and methods.

    Attributes:
        my_attr1 (int): An integer attribute.

    Methods:
        my_meth: A method.

    Example:
        print(lookup(MyClass2))  # Output: A dictionary containing
        the attributes and methods of MyClass2.
    """


class MyClass2(object):
    my_attr1 = 3

    def my_meth(self):
        pass


print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
