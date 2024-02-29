#!/bin/bash
# ALLOWED METHODS
curl -X OPTION -sI $1 | grep -i ALLOW| cut -f2 -d ' '
