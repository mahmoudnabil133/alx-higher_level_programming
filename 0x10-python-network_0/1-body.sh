#!/bin/bash
# size of response
x=$(curl -Is $1| grep -i HTTP | cut -f2 -d ' ')
if [ "$x" == "200" ]; then 
    curl -sI $1
fi
