#!/usr/bin/python3
"""Module that converts a Roman numeral to an integer."""


def roman_to_int(roman_string):
    """Convert a Roman numeral string to an integer.
    Args:
        roman_string (str): the Roman numeral, between 1 and 3999.
    Returns:
        int: the integer value, or 0 if roman_string is not a string.
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    prev_value = 0
    for char in reversed(roman_string):
        value = values.get(char, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
            prev_value = value
    return total
