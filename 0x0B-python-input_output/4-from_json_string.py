#!/usr/bin/python3
"""function returns an object (Python data structure)
represented by a JSON string"""
import json


def from_json_string(my_str):
    """
    Convert a JSON-formatted string to a Python object.

    Parameters:
    - my_str (str): The JSON-formatted string to be
    converted to a Python object.

    Returns:
    - Any: A Python object created from the JSON input.
    """
    return json.loads(my_str)
