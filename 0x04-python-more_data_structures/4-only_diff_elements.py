#!/usr/bin/python3
# This function returns a set of all
# elements present in only one set.
# The Prototype is 'def only_diff_elements(set_1, set_2):'
# Not advised to use any import module.


def only_diff_elements(set_1, set_2):
    return (set_1 ^ set_2)
