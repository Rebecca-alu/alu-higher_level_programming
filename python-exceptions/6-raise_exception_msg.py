#!/usr/bin/python3
"""Module that raises a name exception with a message."""


def raise_exception_msg(message=""):
    """Raise a NameError exception with a message.

    Args:
        message (str): the message of the exception.
    """
    raise NameError(message)
