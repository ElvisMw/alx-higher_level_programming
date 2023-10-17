#!/usr/bin/python3
# This function returns a new dictionary
# with all values multiplied by 2
# Assumption: all values are only integers
# Returns a new dictionary
# Forbidden to import any module


def multiply_by_2(a_dictionary):
    nu_dict = {key: value * 2 for key, value in a_dictionary.items()}
    return nu_dict


def print_sorted_dictionary(a_dictionary):
    _sorted_keys = sorted(a_dictionary.keys())
    for key in _sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
