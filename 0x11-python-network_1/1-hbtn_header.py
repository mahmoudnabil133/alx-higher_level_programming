#!/usr/bin/python3
"""
get item of header
"""
from urllib import request
import sys

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as res:
        print(res.headers["X-Request-Id"])
