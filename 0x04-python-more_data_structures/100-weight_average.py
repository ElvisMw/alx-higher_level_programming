#!/usr/bin/python3
# This function returns the weighted average of
# all integers tuple (<score>, <weight>)
# The Prototype is 'def weight_average(my_list=[]):'
# Returns 0 if the list is empty.
# Forbidden to impport any module.


def weight_average(my_list=[]):
    if not my_list:
        return 0

    the_sum = 0
    total_weight = 0

    for score, weight in my_list:
        the_sum += score * weight
        total_weight += weight

    return (the_sum / total_weight)
