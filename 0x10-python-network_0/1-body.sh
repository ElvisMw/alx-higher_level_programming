#!/bin/bash

# Check if the user provided a URL as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send GET request using curl and store the response body in a variable
response_body=$(curl -s -o /dev/null -w "%{http_code}\n%{body}" "$1")

# Extract status code and body from the response
status_code=$(echo "$response_body" | head -n 1)
body=$(echo "$response_body" | tail -n 1)

# Check if the status code is 200 (OK)
if [ "$status_code" -eq 200 ]; then
  # Display the body if status code is 200
  echo "$body"
else
  # Display an error message for non-200 status codes
  echo "Error: Received status code $status_code"
fi
