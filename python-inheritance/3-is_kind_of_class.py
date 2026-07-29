#!/usr/bin/python3
"""Module that defines the is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of, or inherits from, a_class.

    Args:
        obj: any object.
        a_class: the class to check against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass of it.
    """
    return isinstance(obj, a_class)
