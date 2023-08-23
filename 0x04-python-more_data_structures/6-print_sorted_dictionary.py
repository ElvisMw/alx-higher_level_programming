#!/usr/bin/python3
# This function prints a dictionary by ordered keys.
# Assumption: all keys are strings
# Keys should be sorted by alphabetic order
# Only sort keys of the first level(don’t
# sort keys of a dictionary inside the main dictionary)
# Not allowed to import any module
# Dictionary values can have any type


def print_sorted_dictionary(a_dictionary):
    _sorted_keys = sorted(a_dictionary.keys())
    for key in _sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
