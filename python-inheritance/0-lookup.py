#!/usr/bin/python3
"""Module that defines the lookup function."""
 
 
def lookup(obj):
    """Return the list of available attributes and methods of an object.
 
    Args:
        obj: any object.
 
    Returns:
        list: sorted list of attributes/methods of obj.
    """
    return dir(obj)
