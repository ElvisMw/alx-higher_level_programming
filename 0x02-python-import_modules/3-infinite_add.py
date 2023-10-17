#!/usr/bin/python3
# This program that prints the result of the addition of all arguments
# It can also handle big numbers

import sys

if __name__ == '__main__':
    args = sys.argv[1:]
    total = sum(map(int, args))
    print(total)
