#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        max = a_dictionary[list(a_dictionary)[0]]
        for i in a_dictionary:
            if a_dictionary[i] > max:
                max = a_dictionary[i]
                ret = i
        return (ret)
    return (None)
