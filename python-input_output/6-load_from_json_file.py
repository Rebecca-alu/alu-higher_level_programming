#!/usr/bin/python3
"""Defines a function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Create an Object from a "JSON file"

    Args:
        filename (str): The name of the file to read from
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
