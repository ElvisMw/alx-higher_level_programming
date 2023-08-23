#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda e_l: list(map(lambda y: y**2, e_l)), matrix)))
