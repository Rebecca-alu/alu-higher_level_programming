#!/usr/bin/python3
"""Module that deletes a key in a dictionary."""


def simple_delete(a_dictionary, key=""):
    """Delete a key from a dictionary if it exists.

    Args:
        a_dictionary (dict): the dictionary to update.
        key (str): the key to delete.
    Returns:
        dict: the updated dictionary.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
