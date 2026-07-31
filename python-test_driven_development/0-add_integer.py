#!/usr/bin/python3
"""Module that adds two integers.

This module contains a single function, add_integer, that adds two
numbers together and returns the result as an integer.
"""


def add_integer(a, b=98):
    """Add two integers or floats together.

    Args:
        a (int/float): The first number.
        b (int/float): The second number (default 98).

    Returns:
        int: The sum of a and b, as an integer.

    Raises:
        TypeError: If a or b is not an int or float.
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
