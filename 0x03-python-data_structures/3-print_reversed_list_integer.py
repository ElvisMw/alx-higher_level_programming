#!/usr/bin/python3
"""
- This function prints all integers of a list, in reverse order
- The Prototype used is 'def print_reversed_list_integer(my_list=[]):'
- Not allowed to import any module
- Not allowed to cast integers into strings
"""


def print_reversed_list_integer(my_list=[]):

    for e_num in reversed(my_list):
        print("{:d}".format(e_num))
