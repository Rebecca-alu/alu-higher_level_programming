#!/usr/bin/python3
"""Defines the LockedClass"""


class LockedClass:
    """A class that prevents new instance attributes except first_name"""
    __slots__ = ["first_name"]
