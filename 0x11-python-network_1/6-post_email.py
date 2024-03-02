#!/usr/bin/python3
"post data to server"
import requests
import sys

if __name__ == "__main__":
    dec = {}
    dec['email'] = sys.argv[2]
    res = requests.post(sys.argv[1], data=dec)
    print(res.text)
