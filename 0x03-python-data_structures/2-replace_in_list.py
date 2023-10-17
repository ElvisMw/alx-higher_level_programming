#!/usr/bin/python3
"""
- This function that replaces an element of a list at
a specific position.

- The Prototype used is 'def replace_in_list(my_list, idx, element):'
- If idx is negative then function should not modify anything
and returns the original list
- If idx is out of range (> of number of element in my_list)
then function should not modify anything
and returns the original list
"""


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
