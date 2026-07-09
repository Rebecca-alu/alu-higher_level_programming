#!/usr/bin/python3
"""Module that executes a function safely."""
import sys


def safe_function(fct, *args):
    """Execute a function safely.

    Args:
        fct: a pointer to a function.
        *args: the arguments to pass to fct.

    Returns:
        The result of the function, otherwise None.
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
