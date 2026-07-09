#!/usr/bin/python3
"""Module that safely prints an integer, with an error message."""
import sys


def safe_print_integer_err(value):
    """Print an integer with "{:d}".format().

    Args:
        value: any type of value.

    Returns:
        bool: True if value has been correctly printed, otherwise False.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
