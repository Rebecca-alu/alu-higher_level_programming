#!/usr/bin/python3
"""Module that divides all elements of a matrix by a given divisor."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The divisor.

    Returns:
        list: A new matrix with all elements divided by div, rounded
            to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats,
            if rows are not all the same size, or if div is not a
            number.
        ZeroDivisionError: If div is equal to 0.
    """
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    err_size = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_matrix)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err_matrix)
        for elem in row:
            if not isinstance(elem, (int, float)) or isinstance(elem, bool):
                raise TypeError(err_matrix)

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError(err_size)

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
