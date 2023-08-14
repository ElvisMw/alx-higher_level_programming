#!/usr/bin/python3
""" This function that finds all multiples of 2 in a list
It a new list with True or False, depending if or not
the integer at the same position in the original
list is a multiple of 2.
The new list should have the same size as the original list
"""


def divisible_by_2(my_list=[]):
    result_list = [num % 2 == 0 for num in my_list]
    return result_list
