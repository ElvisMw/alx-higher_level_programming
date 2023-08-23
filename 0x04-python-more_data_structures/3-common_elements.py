#!/usr/bin/python3
# This function returns a set of common
# elements in two sets.
# The Prototype is 'def common_elements(set_1, set_2):'
# Not aloowed to import any module


def common_elements(set_1, set_2):
    common_e = set(filter(lambda x: x in set_1, set_2))
    return common_e
