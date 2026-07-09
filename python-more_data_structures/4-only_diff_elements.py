#!/usr/bin/python3
"""Module that returns a set of all elements present in only one set."""


def only_diff_elements(set_1, set_2):
    """Return a set of elements present in only one of the two sets.
    Args:
        set_1 (set): first set.
        set_2 (set): second set.
    Returns:
        set: elements present in only one set.
    """
    return set_1 ^ set_2
