#!/usr/bin/python3
"""Defines a function that appends a string to the end of a text file"""


def append_write(filename="", text=""):
    """Append a string at the end of a text file (UTF8) and return chars added

    Args:
        filename (str): The name of the file to append to
        text (str): The text to append
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
