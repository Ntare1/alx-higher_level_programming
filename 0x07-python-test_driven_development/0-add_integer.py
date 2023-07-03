#!/usr/bin/python3
""" Module with a function that adds two integers """

def add_integer(a, b=98):
    """ 
    Function add_integer that adds two integers or floats

    Args:
    a: first integer/float
    b: second integer/float

    Returns:
    Addition of the two integers

    Raises: 
    TypeError: in case an of the args is not an integer or float

    """
    if (type(a) != int):
        if (type(a) != float):
            raise TypeError("a must be an integer")
    elif (type(b) != int):
        if (type(b) != float):
            raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
