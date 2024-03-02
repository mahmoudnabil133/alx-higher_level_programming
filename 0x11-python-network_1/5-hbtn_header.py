#!/usr/bin/python3
"desplay value of header"
import requests
import sys

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers["X-Request-Id"])
