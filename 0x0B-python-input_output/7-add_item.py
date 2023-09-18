#!/usr/bin/python3
"""
This script adds command line arguments to a Python list and
saves them to a JSON file.

Usage:
- It loads the existing JSON file 'add_item.json' if it exists and
initializes an empty list if not.
- The script then extends the list with the command line arguments
provided.
- Finally, it saves the updated list to the 'add_item.json' file
using the functions 'save_to_json_file' and
'load_from_json_file' from the respective modules.

Note: This script assumes that the 'save_to_json_file' and
'load_from_json_file' functions exist and can handle JSON file operations
"""

import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])

    save_to_json_file(items, "add_item.json")
