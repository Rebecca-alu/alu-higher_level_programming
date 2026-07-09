#!/usr/bin/python3
"""Module that returns the key with the biggest integer value."""


def best_score(a_dictionary):
    """Return the key with the biggest integer value.
    Args:
        a_dictionary (dict): dictionary with integer values.
    Returns:
        The key with the highest value, or None if no score found.
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
