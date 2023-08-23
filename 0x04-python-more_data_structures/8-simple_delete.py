#!/usr/bin/python3
# This function deletes a key in a dictionary.
# Forbidden to import any module.
# key argument will be always a string
# If a key doesn’t exist, the dictionary won’t change


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary


def print_sorted_dictionary(a_dictionary):
    _sorted_keys = sorted(a_dictionary.keys())
    for key in _sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
