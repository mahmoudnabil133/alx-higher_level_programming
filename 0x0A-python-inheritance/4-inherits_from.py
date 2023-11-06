#!/usr/bin/python3
"""module doc"""


def inherits_from(obj, a_class):
    """ func"""
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
