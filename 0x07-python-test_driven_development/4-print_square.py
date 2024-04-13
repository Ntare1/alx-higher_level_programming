#!/usr/bin/python3
"""
Module that contains a function that prints a square
"""


def print_square(size):
    """
    Function that prints a square using #

    Args:
    size: dictates the size of the square must be an integer

    Raises
    TypeError: size must be an integer
    ValueError: size must be >= 0
    TypeError: size must be an integer

    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if (type(size) == float) and (size < 0):
        raise TypeError("size must be an integer")
    for x in range(size):
        for y in range(size - 1):
            print("#", end="")
        print("#")
