#!/usr/bin/python3
"""Defines a function that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """Read a text file (UTF8) and print it to stdout

    Args:
        filename (str): The name of the file to read
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
