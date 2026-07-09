#!/usr/bin/python3
"""Module that replaces or adds key/value in a dictionary."""


def update_dictionary(a_dictionary, key, value):
    """Replace or add a key/value pair in a dictionary.
    Args:
        a_dictionary (dict): the dictionary to update.
        key (str): the key to add or update.
        value: the value to set for key.
    Returns:
        dict: the updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
