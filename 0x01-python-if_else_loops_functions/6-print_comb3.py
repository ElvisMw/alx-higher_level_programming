#!/usr/bin/python3
# A program that prints all possible different combinations of two digits
# Numbers are separated by "," then  a space
# The two digits must be different
# 01 and 10 are considered the same combination of the two digits 0 and 1
# Code only prints the smallest combination of two digits
# Not allowed to store numbers or strings in a variable
# Not allowed to import any module

for n in range(0, 10):
    for m in range(n + 1, 10):
        if n == 8 and m == 9:
            print("{}{}".format(n, m))
        else:
            print("{}{}".format(n, m), end=", ")
