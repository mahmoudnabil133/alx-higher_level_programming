#!/usr/bin/python3
"""module"""


class BaseGeometry:
    """define a father class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ define a Rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", self.__width)
        self.__width = width
        self.integer_validator("height", self.__height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
