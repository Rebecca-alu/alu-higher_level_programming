#!/usr/bin/python3
"""Defines a function that returns Pascal's triangle of n"""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle

    Args:
        n (int): The number of rows of the triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)
    return triangle
