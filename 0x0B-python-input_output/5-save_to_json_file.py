#!/usr/bin/python3
"""This function handles exceptions related to
    object serialization and file writing."""
import json


def save_to_json_file(my_obj, filename):
    """
    Save a Python object to a JSON file.

    This function takes a Python object and writes it
    to a JSON file in a JSON representation.

    Parameters:
    - my_obj (Any): The Python object to be serialized and
    saved to the file.
    - filename (str): The name of the file to which the
    JSON representation will be saved.
    """
    with open(filename, "w") as fiile:
        json.dump(my_obj, fiile)
