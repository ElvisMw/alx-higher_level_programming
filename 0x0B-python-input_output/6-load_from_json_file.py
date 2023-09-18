#!/usr/bin/python3
"""This function creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """
    Create a Python object from a JSON file.

    This function reads a JSON file and creates a Python object from
    its contents.

    Parameters:
    - filename (str): The name of the JSON file to be read.

    Returns:
    - Any: A Python object created from the JSON file's contents.

    This function does not handle exceptions related to
    missing files or invalid JSON format.

    """
    with open(filename) as e_m:
        return json.load(e_m)
