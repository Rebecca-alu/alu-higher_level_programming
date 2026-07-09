#!/usr/bin/python3
"""Module that prints x elements of a list, safely."""


def safe_print_list(my_list=[], x=0):
    """Print x elements of a list on the same line.

    Args:
        my_list (list): list of any type of elements.
        x (int): number of elements to print.

    Returns:
        int: the real number of elements printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print()
    return count
