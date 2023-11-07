#!/usr/bin/python3
"""this is module"""


def write_file(filename="", text=""):
    """define a function"""
    with open(filename, "w", encodein="utf-8") as file:
        return file.write(text)
