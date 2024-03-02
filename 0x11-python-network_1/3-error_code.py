#!/usr/bin/python3
"""
handle error
"""
from urllib import request
import urllib
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read())
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
