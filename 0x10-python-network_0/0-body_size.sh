#!/usr/bin/env bash
# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url=$1

# Use curl to send a request and display the size of the response body in bytes
size=$(curl -sI "$url" | grep -i "content-length" | awk '{print $2}' | tr -d '\r')

# Check if the size is empty
if [ -z "$size" ]; then
    echo "Unable to determine the size of the response body."
else
    echo "$size"
fi
