#!/usr/bin/python3
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

    url = "https://api.github.com/user"
    response = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    try:
        user_data = response.json()
        print(user_data["id"])
    except Exception as e:
       print(None)
