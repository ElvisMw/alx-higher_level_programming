#!/usr/bin/python3
# This program prints the number of and the list of its arguments
# This code does not execute when imported

import sys

if __name__ == '__main__':
    number_args = len(sys.argv) - 1

    if number_args == 0:
        print("0 arguments.")
    elif number_args == 1:
        print("1 argument:")
    else:
        print(f"{number_args} arguments:")

    for e in range(1, number_args + 1):
        print(f"{e}: {sys.argv[e]}")
