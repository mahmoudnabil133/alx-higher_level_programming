#!/usr/bin/python3
"fetch url using"
import requests

if __name__ == "__main__":
    res = requests.get("https://alx-intranet.hbtn.io/status")
    print("\t- type: {}".format(type(res.text)))
    print("\t- type: {}".format(res.status_code))
