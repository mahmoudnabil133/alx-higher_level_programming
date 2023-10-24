#!/usr/bin/python3
""" define a class"""


class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an intiger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
