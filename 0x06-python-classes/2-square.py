#!/usr/bin/python3
"""defining  class square"""


class Square:
    """defining object size"""

    def __init__(self, size=0):
        """initializing object size"""
        if type(size) is int:
            pass

        else:
            raise TypeError("size must be an integer")
        if size >= 0:
            self.__size = size

        else:
            raise ValueError("size must be >= 0")
