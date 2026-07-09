#!/usr/bin/python3
"""Module that squares all integers of a matrix."""


def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix.
    Args:
        matrix (list): a 2 dimensional array of integers.
    Returns:
        list: a new matrix, same size, with each value squared.
    """
    return [list(map(lambda x: x ** 2, row)) for row in matrix]
