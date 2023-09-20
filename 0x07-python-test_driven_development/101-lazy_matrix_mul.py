#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a: The first matrix.
        m_b: The second matrix.

    Returns:
        The result of the matrix multiplication.
    """
    return np.dot(m_a, m_b)

if __name__ == "__main__":
    m1 = [[1, 2], [3, 4]]
    m2 = [[1, 2], [3, 4]]
    result = lazy_matrix_mul(m1, m2)
    print(result)

    m3 = [[1, 2]]
    m4 = [[3, 4], [5, 6]]
    result2 = lazy_matrix_mul(m3, m4)
    print(result2)
