#!/usr/bin/python3
# - This function computes the square value of all integers of a matrix.
# - matrix is a 2 dimensional arrayPrototype: def square_matrix_simple(mat


def square_matrix_simple(matrix=[]):

    new_matrix = []

    for row in matrix:
        new_row = []
        for number in row:
            new_row.append(number ** 2)
        new_matrix.append(new_row)
    return new_matrix


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
