#!/usr/bin/python3
"""Module that adds all unique integers in a list."""


def uniq_add(my_list=[]):
    """Add all unique integers in a list (only once for each integer).
    Args:
        my_list (list): list of integers.
    Returns:
        int: sum of unique integers.
    """
    return sum(set(my_list))
