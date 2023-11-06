#!/usr/bin/python3
"""module"""


class BaseGeometry:
    """define a class"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if type(value) <= 0:
            raise TypeError("{} must be greater than 0".format(name))
