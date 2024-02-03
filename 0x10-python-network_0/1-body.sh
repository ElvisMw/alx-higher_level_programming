#!/bin/bash
# This script takes in a URL, sends a GET request, and displays the body of the response for a 200 status code

response=$(curl -sL -w "%{http_code}\n" "$1")

status_code=$(tail -n1 <<< "$response")
body=$(sed '$d' <<< "$response")

if [[ "$status_code" == 200 ]]; then
    echo "$body"
else
    echo "Unexpected status code: $status_code"
fi
