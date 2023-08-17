#!/usr/bin/python3
# - This function computes the square value of all integers of a matrix.
# - matrix is a 2 dimensional arrayPrototype: def square_matrix_simple(mat


def square_matrix_simple(matrix=[]):
    new_matrix = list(map(lambda row: list(map(lambda numb: numb ** 2, row)), matrix))
    return new_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
