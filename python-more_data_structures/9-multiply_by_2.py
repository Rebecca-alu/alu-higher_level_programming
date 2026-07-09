#!/usr/bin/python3
"""Module that multiplies all values of a dictionary by 2."""


def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multiplied by 2.
    Args:
        a_dictionary (dict): dictionary with integer values.
    Returns:
        dict: a new dictionary with doubled values.
    """
    return {key: value * 2 for key, value in a_dictionary.items()}
