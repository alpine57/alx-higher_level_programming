#!/usr/bin/python3
"""
module contains a class rectangle that defines a rectangle
"""


class Rectangle:
    """
   defines an a class rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes private instance width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrive the private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value for width,with typeerro and valueerror"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrives the private instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value for width,with typeerro and valueerror"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Get the area of the rectangle class width * height"""
        return self.__width * self.__height

    def perimeter(self):
        """Get the perimeter of the rectangle class width(2) + height(2)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """returns the rectangle in the form #"""

        if self.__height == 0 or self.__width == 0:
            return ''

        string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            if i < self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """Return a string of an object of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """deletes an instance rectangle and prints bye rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

