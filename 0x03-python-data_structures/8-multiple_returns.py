#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght == 0:
        return None
    f_char = sentence[0]
    t = (lenght, f_char)
    return t
