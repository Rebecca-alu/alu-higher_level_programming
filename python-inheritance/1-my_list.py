#!/usr/bin/python3
"""Defines the MyList class"""


class MyList(list):
    """Represent a list, with an additional sorted-print method"""

    def print_sorted(self):
        """Print the list, sorted in ascending order"""
        print(sorted(self))
