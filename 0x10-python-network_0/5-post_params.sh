#!/usr/bin/env bash
# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url=$1

# Variables for POST parameters
email="test@gmail.com"
subject="I will always be here for PLD"

# Use curl to send a POST request with the specified parameters and display the body
curl -s -X POST -d "email=$email&subject=$subject" "$url"
