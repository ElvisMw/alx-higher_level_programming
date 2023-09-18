#!/usr/bin/python3
"""This function that multiplies 2 matrices:and
Prototype: def matrix_mul(m_a, m_b):"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns the result.

    Args:
    m_a (list of lists): The first matrix represented as a
    list of lists of integers or floats.
    m_b (list of lists): The second matrix represented as a
    list of lists of integers or floats.

    Returns:
    list of lists: The resulting matrix as a list of lists of
    integers or floats.

    Raises:
    TypeError: If m_a or m_b is not a list, not a list of lists, or
    contains non-integer and non-float elements.
    ValueError: If m_a or m_b is empty (an empty list or a list of
    empty lists) or if the matrices cannot be multiplied.
    """

    # Check if m_a and m_b are lists
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list and m_b must be a list")

    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists and m_b must be a list of lists")

    # Check if m_a and m_b are not empty
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty and m_b can't be empty")

    # Check if all elements are integers or floats
    for row in m_a:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_b should contain only integers or floats")

    # Check if both matrices are rectangular
    if len(set(len(row) for row in m_a)) != 1 or len(set(len(row) for row in m_b)) != 1:
        raise TypeError("Each row of m_a and m_b must be of same size")

     # Check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for e_m in range(len(m_a)):
        row = []
        for b in range(len(m_b[0])):
            element = sum(m_a[e_m][k] * m_b[k][b] for k in range(len(m_a[0])))
            row.append(element)
        result.append(row)

    return result
