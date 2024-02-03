#!/bin/bash
# This script takes a URL as an argument, sends a GET request to the URL using curl in silent mode, and displays the body of the response only for a 200 status code.

curl -s -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
