#!/usr/bin/python3
"""function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, att, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj (object): The object to which the attribute should be added.
        att (str): The name of the attribute to add.
        value (any): The value to assign to the new attribute.

    Raises:
        TypeError: If the object can't have new attributes.

    Example:
        class MyClass():
            pass

        mc = MyClass()
        add_attribute(mc, "name", "John")
        print(mc.name)

        try:
            a = "My String"
            add_attribute(a, "name", "Bob")
            print(a.name)
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
