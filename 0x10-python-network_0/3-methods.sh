#!/usr/bin/bash
# Check if the correct number of arguments is provided

# Get the URL from the command line argument
url=$1

# Use curl to send an OPTIONS request and display the Allow header
curl -sI -X OPTIONS "$url" | grep -i "Allow" | cut -d ":" -f 2- | cut -c 2-
