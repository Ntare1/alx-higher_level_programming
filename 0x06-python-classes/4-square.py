#!/usr/bin/python3
""" module defining a square """


class Square:
    """Class of a square"""

    def __init__(self, size=0):
        """Method initializing class
         Args:
         size: private attribute showing size of the square
           """
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
        
        """ method representing area of the square"""
    def area(self):
        self.area = self.__size * self.__size
