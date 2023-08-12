#!/usr/bin/python3
# This function removes all characters 'c' & 'C" from a string
# The Prototype is 'def no_c(my_string):'
"""The function returns the new string
- Not allowed to import any module
- Not allowed to use str.replace()
"""


def no_c(my_string):
    nu_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            nu_string += char
    return nu_string
