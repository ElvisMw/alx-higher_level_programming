#!/usr/bin/python3
# Prototype: def uppercase(str):
# Only use no more than 2 print functions with string format
# Only use one loop in your code
# Not allowed to import any module
# Not allowed to use str.upper() and str.isupper()

def uppercase(str):
    for chu in str:
        if ord(chu) >= 97 and ord(chu) <= 122:
            chu = chr(ord(chu) - 32)
        print("{}".format(chu), end="")
