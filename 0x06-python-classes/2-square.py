#!/usr/bin/python3
""" Class defining a square """


class Square:
    def __init__(self, size=0):
        self.__size = size
        """ raising exceptions incase size in not an integer or below """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
