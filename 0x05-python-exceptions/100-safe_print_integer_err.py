#!/usr/bin/python3
# This function prints an integer.
# The prototype is: def safe_print_integer_err(value):
# value can be any type (integer, string, etc.)
# The integer should be printed followed by a new line
# Returns True if value has been correctly
# printed (it means the value is an integer)
# Otherwise, returns False and prints in
# stderr the error precede by Exception:
# try: / except: is used
# "{:d}".format() to print as integer is used
# Not allowed to use type()


import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
