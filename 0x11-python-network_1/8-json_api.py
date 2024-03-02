#!/usr/bin/python3
"handle error"
import requests
import sys

if __name__ == "__main__":
    try:
        if len(sys.argv) <= 1:
            val = ""
        else:
            val = sys.argv[1]
        req = requests.post("http://0.0.0.0:5000/search_user", {"q": val})
        res = req.json()
        if not res:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except Exception as e:
        print("Not a valid JSON")
