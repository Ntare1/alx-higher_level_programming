#!/usr/bin/python3
"""
Module containg a function that  returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """
    Function returns a list of available
    attribute and methods of an object
    """
    return(dir(obj))
