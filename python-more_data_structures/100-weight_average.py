#!/usr/bin/python3
"""Module that returns the weighted average of a list of (score, weight)."""


def weight_average(my_list=[]):
    """Return the weighted average of all integer tuples (score, weight).
    Args:
        my_list (list): list of (score, weight) tuples.
    Returns:
        float: the weighted average, or 0 if the list is empty.
    """
    if not my_list:
        return 0
    total_score = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for score, weight in my_list)
    return total_score / total_weight
