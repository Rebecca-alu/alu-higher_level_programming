#!/usr/bin/python3
"""Module that defines the is_same_class function."""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class.

    Args:
        obj: any object.
        a_class: the class to check against.

    Returns:
        bool: True if type(obj) is exactly a_class, else False.
    """
    return type(obj) is a_class
