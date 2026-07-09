#!/usr/bin/python3
"""Module that reproduces a given Python bytecode as a function."""


def magic_calculation(a, b):
    """Perform the calculation described by the given bytecode.

    Args:
        a (int): first value.
        b (int): second value.

    Returns:
        The result of the calculation.
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            result += (a ** b) / i
        except Exception:
            result = b + a
            break
    return result
