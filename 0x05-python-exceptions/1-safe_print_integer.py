#!/usr/bin/python3
# This function that prints an integer with "{:d}".format()
# The prototype is - def safe_print_integer(value):
# value can be any type (integer, string, etc.)
# The integer should be printed followed by a new line
# Returns True if value has been correctly printed
# (it means the value is an integer)
# Otherwise, returns False
# try: / except: -is used
# "{:d}".format() to print as integer is used
# not allowed to import any module
# not allowed to use type()

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
