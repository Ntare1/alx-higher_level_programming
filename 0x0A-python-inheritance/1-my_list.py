#!/usr/bin/python3
"""
module containing class Mylist that inherits from list
"""


class MyList(list):
    """Class Mylist that inherits from list"""
    def print_sorted(self):
        """Function prints the list sorted"""
        print(sorted(self))