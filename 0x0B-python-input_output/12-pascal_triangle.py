#!/usr/bin/python3
"""This is a function def pascal_triangle(n) """


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    This function calculates and returns a list of lists of
    integers representing Pascal's triangle up to the nth row.
    Each row is represented as a list of integers.

    Parameters:
    - n (int): The number of rows to generate in Pascal's triangle.

    Returns:
    - List[List[int]]: A list of lists representing Pascal's triangle.

    Returns an empty list if n <= 0.
    Assumes n will always be an integer.

    Example:
    >>> print_triangle(pascal_triangle(5))
    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        nu_triangl = triangles[-1]
        tmp = [1]
        for e_m in range(len(nu_triangl) - 1):
            tmp.append(nu_triangl[e_m] + nu_triangl[e_m + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
