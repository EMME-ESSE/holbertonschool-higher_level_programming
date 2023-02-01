#!/usr/bin/python3
'''class rectangle '''


class Rectangle:
    '''rectangle'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    '''getter width'''
    @property
    def width(self):
        return self.__width
    ''' setter width '''
    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
    '''getter height'''
    @property
    def height(self):
        return self.__height
    ''' setter size '''
    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
    '''calculation'''
    def area(self):
        return self.__width * self.__height
    '''calculation'''
    def perimeter(self):
        if self.__height is 0 or self.__width is 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
    '''print the rectangle'''
    def __str__(self):
        a = ""
        if self.__height is 0 or self.__width is 0:
            return ""
        for x in range(self.__height):
            a += ("#" * self.__height) 
            if (x < self.__width -1):
                a += ("\n")
        return a
