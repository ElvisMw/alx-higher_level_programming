#!/usr/bin/python3
# This function divides 2 integers and prints the result.
# The Prototype is: def safe_print_division(a, b):
# Assumption: Both a and b are integers.
# The result of the division should
# print on the finally: section preceded by Inside result:
# Returns the value of the division, otherwise: None
# use try: / except: / finally:
# use "{}".format() to print the result
# not allowed to import any module

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
