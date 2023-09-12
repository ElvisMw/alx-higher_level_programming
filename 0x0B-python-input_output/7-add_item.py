#!/usr/bin/python3
"""Adds command line arguments to a list and saves it to a JSON file."""

import sys
import os.path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


if __name__ == "__main__":
    """
    This script adds command line arguments to a list and
    saves it to a JSON file.

    Usage:
    - If the JSON file 'add_item.json' exists, it loads its
    contents into a list.
    - If the file does not exist, it initializes an empty list.
    - Then, it extends the list with the command line arguments provided.
    - Finally, it saves the updated list to the 'add_item.json' file.

    This script depends on the 'save_to_json_file' and
    'load_from_json_file' functions.
    """

    json_file = "add_item.json"

    if os.path.exists(json_file):
        my_list = load_from_json_file(json_file)
    else:
        my_list = []

    my_list.extend(sys.argv[1:])

    save_to_json_file(my_list, json_file)
