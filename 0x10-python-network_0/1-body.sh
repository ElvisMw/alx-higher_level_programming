#!/bin/bash
# This script takes in a URL, sends a GET request, and displays the body of the response for a 200 status code

response=$(curl -sL -w "%{http_code}" "$1")

status_code=$(tail -n1 <<< "$response")
body=$(sed '$d' <<< "$response")

if [ "$status_code" -eq 200 ]; then
    echo "$body"
fi
