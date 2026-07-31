#!/usr/bin/python3
"""Module that prints a full name.
"""


def say_my_name(first_name, last_name=""):
    """Print 'My name is <first_name> <last_name>'.

    Args:
        first_name: string, the first name.
        last_name: string, the last name, defaults to an empty string.

    Raises:
        TypeError: if first_name is not a string, or if last_name is
            not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
