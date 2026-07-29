#!/usr/bin/python3
"""Module that defines the inherits_from function."""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherited from a_class.

    Args:
        obj: any object.
        a_class: the class to check against.

    Returns:
        bool: True if obj's class inherits (directly or indirectly)
              from a_class, but is not a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
