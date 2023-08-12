#!/usr/bin/python3
"""
- This function that replaces an element in a list at
a specific position without modifying the original list

- The Prototype is 'def new_in_list(my_list, idx, element):'
- If idx is negative, the function returns
a copy of the original list
- If idx is out of range (> of number of element in my_list)
then function returns a copy of the original list
"""


def new_in_list(my_list, idx, element):

    if idx < 0 or idx >= len(my_list):
        return my_list[:]

    nu_list = my_list[:]
    nu_list[idx] = element
    return nu_list
