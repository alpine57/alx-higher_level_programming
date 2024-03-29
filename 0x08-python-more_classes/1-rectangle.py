#!/usr/bin/python3
"""
module contains a class rectangle that defines a rectangle
"""


class Rectangle:
    """
   define class rectangle
    """

    def __init__(self, width=0, height=0):
        """initialize private instance width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrive private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets value for width,with type erro and value error"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrives  private instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets value for width,with typeerro and valueerror"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

