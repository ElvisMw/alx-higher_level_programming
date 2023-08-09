#!/usr/bin/python3
# Prototype: def uppercase(str):
# Only use no more than 2 print functions with string format
# Only use one loop in your code
# Not allowed to import any module
# Not allowed to use str.upper() and str.isupper()

def uppercase(str):
    for char in str:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
