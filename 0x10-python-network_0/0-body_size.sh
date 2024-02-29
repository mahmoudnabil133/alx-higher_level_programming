#!/bin/bash
# size of response
echo curl $1 | grep -i content-lenght |  awk '{print $2}'
