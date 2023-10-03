#!/usr/bin/python3
for i in range(100):
    if i % 11 == 0:
        continue
    if i == 89:
        print("{:02d}".format(i))
        break
    print("{:02d}".format(i), end=", ")
