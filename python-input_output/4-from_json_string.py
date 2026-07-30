#!/usr/bin/python3
"""Defines a function that returns an object from a JSON string"""
import json


def from_json_string(my_str):
    """Return an object (Python data structure) from a JSON string

    Args:
        my_str (str): The JSON string to deserialize
    """
    return json.loads(my_str)
