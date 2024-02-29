#!/bin/bash
# size of response
curl -sI $1 | grep -i Content-Length| cut -f2 -d ' '
