"""
- This functionprints a matrix of integers using prototype
def print_matrix_integer(matrix=[[]]).
- not allowed to import any module and to
cast integers into strings.
- Assumption: List has integers only.
"""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for e, num in enumerate(row):
            print("{:d}".format(num), end="")
            if e < len(row) - 1:
                print(" ", end="")
        print()
