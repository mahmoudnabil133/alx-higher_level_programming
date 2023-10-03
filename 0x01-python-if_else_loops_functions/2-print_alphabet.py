#!/usr/bin/python3
a = 'abcdefghijklmnopqrstuvwxyz'
i = 0
while (True):
    print("{}".format(a[i]), end="")
    if a[i] == 'z':
        break
    i += 1
