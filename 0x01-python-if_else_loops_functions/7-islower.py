#!/usr/bin/python3
# A function that checks for lowercase character
# The Prototype: def islower(c):Returns True if c is lowercase
# The code returns False otherwise
# Not allowed to import any module
# Not allowed to use str.upper() and str.isupper()

def islower(c):
    ascii_value = ord(c)
    if 97 <= ascii_value <= 122:
        return True
    else:
        return False
