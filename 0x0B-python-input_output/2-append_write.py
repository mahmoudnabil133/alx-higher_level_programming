#!/usr/bin/python3
"""this is module"""


def append_write(filename="", text=""):
    """define a function"""

    with open(filename, 'a') as f:
        return f.write(text)
