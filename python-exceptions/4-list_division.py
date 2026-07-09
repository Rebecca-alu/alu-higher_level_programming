#!/usr/bin/python3
"""Module that divides element by element 2 lists."""


def list_division(my_list_1, my_list_2, list_length):
    """Divide element by element two lists.

    Args:
        my_list_1 (list): the list of numerators.
        my_list_2 (list): the list of denominators.
        list_length (int): the length of the new list.

    Returns:
        list: a new list with all divisions.
    """
    new_list = []
    for i in range(list_length):
        div = 0
        try:
            div = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(div)
    return new_list
