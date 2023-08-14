#!/usr/bin/python3
""" This function that deletes the item at a
specific position in a list. Not allowed to use pop() or
to import any module.
- Prototype to be used is: def delete_at(my_list=[], idx=0):
"""


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list

    my_new_list = [item for e, item in enumerate(my_list) if e != idx]
    return my_new_list
