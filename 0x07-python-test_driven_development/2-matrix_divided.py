#!/usr/bin/python3
"""
Module that contains a function that divides elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Function divides a matrix with an integer or float

    Args:
    matrix: a list of list
    div: a float/ integer that will divide the matrix

    Returns: A new matrix

    Raises:
    TypeError: Each row of the matrix must have the same size
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    TypeError: div must be a number

    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(message)
    lst_len = len(matrix[0])
    new_matrix = []
    for lst in matrix:
        if len(lst) != lst_len:
            raise TypeError("Each row of the matrix must have the same size")
        new_list = []
        for item in lst:
            if not type(div) in (int, float):
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            if not type(item) in (int, float):
                raise TypeError(message)
            new_list.append(round(item / div, 2))
        new_matrix.append(new_list)
    return(new_matrix)
