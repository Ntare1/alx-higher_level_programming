#!/usr/bin/python3
""" module defining a square """


class Square:
    """Class of a square"""
    def __init__(self, size=0, position=(0, 0)):
        """ Method initializing class
        Args:
        size: private attribute showing size of the square
        position:
        Raises:
        TypeError: in case size is not an integer
        ValueError: in case siz is less than zero
        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    """ method representing area of the square"""
    def area(self):
        return (self.__size * self.__size)

    """ method to print the square in # """
    def my_print(self):
        if (self.__size == 0):
            print('')
        else:
            for x in range(self.__size):
                print("#" * self.__size)
