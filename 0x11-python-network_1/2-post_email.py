#!/usr/bin/python3
"""
get item of header
"""
from urllib import request
from urllib import parse
import sys

if __name__ == "__main__":
    dec = {}
    dec['email'] = sys.argv[2]
    encoded_data = parse.urlencode(dec).encode("utf-8")
    with request.urlopen(sys.argv[1], data=encoded_data) as res:
        body = res.read().decode("utf-8")
