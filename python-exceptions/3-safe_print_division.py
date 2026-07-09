#!/usr/bin/python3
"""Module that divides 2 integers and prints the result."""


def safe_print_division(a, b):
    """Divide a by b and print the result.

    Args:
        a (int): the dividend.
        b (int): the divisor.

    Returns:
        The value of the division, otherwise None.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
