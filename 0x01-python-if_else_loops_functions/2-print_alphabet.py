#!/usr/bin/python3
# a program that prints the ASCII alphabet,
# in lowercase, not followed by a new line.
# Using only 1 loop, 1 print function with string format
# not allowed to store characters in a variable
# not allowed to import any module.

for e in range(97, 123):
    print("{}".format(chr(e)), end='')
