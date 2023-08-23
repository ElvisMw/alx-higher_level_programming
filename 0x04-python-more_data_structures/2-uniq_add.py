#!/usr/bin/python3
# This function that adds all unique integers
# in a list (only once for each integer).
# The Prototype is 'def uniq_add(my_list=[]):'
# Not allowed to import any module


def uniq_add(my_list=[]):
    unique_numbers = set(my_list)
    total = sum(unique_numbers)
    return total
