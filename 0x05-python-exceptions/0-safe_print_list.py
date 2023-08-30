#!/usr/bin/python3
# This function that prints x elements of a list.
# The prototype is def safe_print_list(my_list=[], x=0):
# All elements must be printed on the same line followed by a new line.
# x represents the number of elements to print
# x can be bigger than the length of my_list
# Returns the real number of elements printed
# try: / except: is used
# not allowed to import any module
# not allowed to use len()

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for e in range(x):
            print(my_list[e], end='')
            count += 1
    except IndexError:
        pass
    finally:
        print()
        return count
