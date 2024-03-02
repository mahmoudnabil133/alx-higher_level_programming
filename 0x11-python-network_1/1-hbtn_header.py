#!usr/bin/python3
from urllib import request
import sys
"fethch url"

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as res:
        val = res.headers["X-Request-Id"]
        print(val)
