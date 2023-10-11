#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dec2 = a_dictionary.copy()
    for i in dec2:
        dec2[i] *= 2
    return (dec2)
