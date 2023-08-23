#!/usr/bin/python3
# This function replaces or adds key/value in a dictionary
# 'key' argument will be always a string
# 'value' argument will be any type
# If a key exists in the dictionary,
# the value will be replaced.
# If a key doesn’t exist in the dictionary,
# it will be created.
# Forbidden to import any module


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary


def print_sorted_dictionary(a_dictionary):
    _sorted_keys = sorted(a_dictionary.keys())
    for key in _sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
