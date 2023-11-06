#!/usr/python3
""" my module"""


class MyList(list):
    """ define a class"""
    def print_sorted(self):
        print (sorted(list(self)))
