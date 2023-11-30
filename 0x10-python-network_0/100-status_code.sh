#!/usr/bin/bash
# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url=$1

# Use curl to send a request and display only the status code
curl -s -o /dev/null -w "%{http_code}" "$url"
