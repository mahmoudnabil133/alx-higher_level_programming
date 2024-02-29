#!/bin/bash
# ALLOWED METHODS
curl -X OPTION -sI $1 | grep -i Allow| cut -f2- -d ' '
