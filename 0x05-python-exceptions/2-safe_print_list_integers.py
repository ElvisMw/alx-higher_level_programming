#!/usr/bin/python3
# This function prints the first x elements of a list and only integers
# Prototype: def safe_print_list_integers(my_list=[], x=0):
# my_list can contain any type (integer, string, etc.)
# All integers have to be printed on the same line followed by
# a new line - other type of value in the list must be
# skipped (in silence).
# x represents the number of elements to access in my_list
# x can be bigger than the length of my_list -if it’s
# the case, an exception is expected to occur
# Returns the real number of integers printed
# try: / except: must be used
# "{:d}".format() to print an integer must be used
# not allowed to import any module
# not allowed to use len()

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for item in my_list:
            if count == x:
                break

            if isinstance(item, int):
                print("{:d}".format(item), end=' ')
                count += 1
    except IndexError:
        pass
    finally:
        print()
        return count
