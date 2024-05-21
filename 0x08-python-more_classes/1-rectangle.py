#!/usr/bin/python3
"""define a class rectangle"""


class Rectangle:
    """represent a rectangle"""

    def __init__(self, width=0, height=0):
        """initialize a new rectangle
        Args:
             length: longer dimension of rectangle
             width: shorter dimension of rectangle
            """
        self.___width = width
        self.__height = height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def  height(self):
        return self.__height
    @width.setter
    def height(self, value):
         if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
