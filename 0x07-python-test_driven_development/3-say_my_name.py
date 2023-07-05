#!/usr/bin/python3
"""
Module that prints the first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Function prints the first and last name

    Args:
    first_name: should be a string
    last_name: should be a string 

    Return: a string containg the first and last name

    Raises:
    TypeError: first_name must be a string or last_name must be a string

    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")