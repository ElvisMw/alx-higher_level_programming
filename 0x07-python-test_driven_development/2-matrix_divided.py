#!/usr/bin/python3
"""This function divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number to divide the elements of the matrix by.

    Returns:
        list of lists: A new matrix with elements divided by
        `div` rounded to 2 decimal places.

    Raises:
        TypeError: If `matrix` is not a list of lists of integers or floats,
                   if rows of the matrix have different sizes,
                   or if `div` is not a number.
        ZeroDivisionError: If `div` is equal to 0.
    """

    """Check whether the list's matrix is a lists of numbers(integers or
    floats)"""
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or \
       not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    """Check whether the rows of the matrix are of same size"""
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    """Check whether div is an integer or float)"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    """ Divides each matrix's element by div, and rounded to two decimal
    places"""
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
