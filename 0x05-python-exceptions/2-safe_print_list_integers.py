#!/usr/bin/python3
# This function that prints the first x elements of a list
# and only integers.
# The Prototypeis : def safe_print_list_integers(my_list=[], x=0):
# my_list can contain any type (integer, string, etc.)

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for item in my_list:
            if count == x:
                break

            if isinstance(item, int):
                print("{:d}".format(item), end=' ')
                count += 1
    except TypeError:
        pass
    except IndexError:
        print()  # Print a newline before raising the exception
        raise
    finally:
        print()
        return count
