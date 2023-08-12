#!/usr/bin/python3
"""This python code prints all integers of a
list. With the format of an integer per line.
No importing any module.
"""


def print_list_integer(my_list=[]):
    for e_num in my_list:
        print("{:d}".format(e_num))
