#!/usr/bin/python3
# - This functionprints a matrix of integers using prototype
# def print_matrix_integer(matrix=[[]]).


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for e, num in enumerate(row):
            print("{:d}".format(num), end="")
            if e < len(row) - 1:
                print(" ", end="")
        print()
