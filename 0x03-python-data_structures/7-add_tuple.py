#!/usr/bin/python3
""" This function adds 2 tuples and returns
a tuple with two integers"""


def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    summation_of_first_elements = a[0] + b[0]
    summation_of_second_elements = a[1] + b[1]

    result_tuple = (summation_of_first_elements, summation_of_second_elements)
    return result_tuple
