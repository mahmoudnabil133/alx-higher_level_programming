#!/usr/bin/python3
"""
fetch the url
"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        body = res.read()
        print("Body response:")
        print('\t- type: {}'.format(type(body)))
        print('\t- type: {}'.format(body))
        print('\t- type: {}'.format(body.decode("utf-8")))
