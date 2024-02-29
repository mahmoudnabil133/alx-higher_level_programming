#!/bin/bash
# size of response
x=$(curl -sI $1 | grep -i Content-Length| cut -f2 -d ' ')
echo $x
