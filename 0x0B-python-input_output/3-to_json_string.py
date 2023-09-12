#!/usr/bin/python3
"""This function returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """
    Convert a Python object to a JSON-formatted string.

    Parameters:
    - my_obj (Any): The Python object to be converted to a JSON string.

    Returns:
    - str: A JSON-formatted string representation of the input object.
    """
    return json.dumps(my_obj)
