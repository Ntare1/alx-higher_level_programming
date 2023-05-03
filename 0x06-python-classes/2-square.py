#!/usr/bin/python3
""" module defining a square """


class Square:
    def __init__(self, size=0):
        """ Initializing a class square
        Args:    
        size: private atrribute showing the size of square
        Raises:
        TypeError: when the size is not an integer
        ValueError: when size is less than zero
        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

