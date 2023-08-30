#!/usr/bin/python3
# This function that prints the first x elements of a list
# and only integers.
# The Prototypeis : def safe_print_list_integers(my_list=[], x=0):
# my_list can contain any type (integer, string, etc)

def safe_print_list_integers(my_list=[], x=0):
    integer_count = 0
    for e in range(0, x):
        try:
            print("{:d}".format(my_list[e]), end="")
            integer_count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return integer_count
