#!/usr/bin/python3
"""
- The Prototype used is 'def element_at(my_list, idx):'
- If idx is negative then function returs 'None'
- If idx is out of range (> of number of element in my_list)
then function returns 'None'
"""


def element_at(my_list, idx):

    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
