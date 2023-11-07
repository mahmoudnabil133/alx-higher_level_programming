#!/usr/bin/python3
"""this is module"""


def write_file(filename="", text=""):
    """define a function"""
    with open(filename, "w") as file:
        return file.write(text)
