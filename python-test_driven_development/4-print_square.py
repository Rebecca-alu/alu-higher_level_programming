#!/usr/bin/python3
"""Module that prints a square with the character #."""


def print_square(size):
    """Print a square of the given size using the character #.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer (or is a negative float).
        ValueError: If size is a negative integer.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
