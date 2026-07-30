#!/usr/bin/python3
"""Defines a function that returns the dictionary description of an object"""


def class_to_json(obj):
    """Return the dictionary description of a simple data structure object

    Args:
        obj: An instance of a Class whose attributes are all serializable
    """
    return obj.__dict__
