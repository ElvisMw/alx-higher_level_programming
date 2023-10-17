#!/usr/bin/python3
# - This function computes the square value of all integers of a matrix.
# - matrix is a 2 dimensional arrayPrototype: def square_matrix_simple(mat


def square_matrix_simple(matrix=[]):
    nu_matrix = matrix.copy()

    for e in range(len(matrix)):
        nu_matrix[e] = list(map(lambda x: x**2, matrix[e]))

    return (nu_matrix)
