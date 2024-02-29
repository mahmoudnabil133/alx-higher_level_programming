#!/bin/bash
# ret
if [ $(curl -L -s -X HEAD -w "%{http_code}" "$1") == '200' ]; then 
    curl -sL $1
fi
