#!/usr/bin/python3
# - This function computes the square value of all integers of a matrix.
# - matrix is a 2 dimensional arrayPrototype: def square_matrix_simple(mat


def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for e_j in range(len(matrix)):
        new_matrix[e_j] = list(map(lambda x: x**2, matrix[e_j]))

    return (new_matrix)
