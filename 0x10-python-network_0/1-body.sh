#!/bin/bash
# This script takes in a URL, sends a GET request, and displays the body of the response for a 200 status code

response=$(curl -sL -w "%{http_code}" "$1")

status_code=$(tail -c 4 <<< "$response")
body=$(sed '$s/^[0-9]\{3\}//' <<< "$response")

if [[ "$status_code" == 200 ]]; then
    echo "$body"
else
    echo "Unexpected status code: $status_code"
fi
