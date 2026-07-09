#!/usr/bin/python3
"""Module that safely prints an integer."""


def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
        value: any type of value.

    Returns:
        bool: True if value has been correctly printed, otherwise False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
