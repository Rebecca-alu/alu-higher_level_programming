#!/usr/bin/python3
"""Module that prints the first x elements of a list, integers only."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list, printing only integers.

    Args:
        my_list (list): list of any type of elements.
        x (int): number of elements to access in my_list.

    Returns:
        int: the real number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
