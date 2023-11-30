#!/usr/bin/env bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url=$1

# Use curl to send a GET request and display the body if the status code is 200
body=$(curl -s -o /dev/null -w "%{http_code}" "$url")

if [ "$body" -eq 200 ]; then
    curl -s "$url"
else
    echo "Error: Received status code $body"
fi
