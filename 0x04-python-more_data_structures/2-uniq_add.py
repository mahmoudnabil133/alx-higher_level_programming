#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_set = set(my_list)
    sum = 0
    for i in uniq_set:
        sum += i
    return sum
