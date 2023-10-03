#!/usr/bin/python3
a = 'abcdfghijklmnoprstuvwxyz'
i = 0
while (True):
    print(f"{a[i]}", end="")
    if a[i] == 'z':
        break
    i += 1
