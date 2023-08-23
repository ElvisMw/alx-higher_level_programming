#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [list(map(lambda e_l: e_l * e_l, row)) for row in matrix]
