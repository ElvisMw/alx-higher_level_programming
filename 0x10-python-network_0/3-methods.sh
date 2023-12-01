#!/usr/bin/bash
# Check if the correct number of arguments is provided
curl -sI -X OPTIONS $1 | grep -i "Allow" | cut -d ":" -f 2- | cut -c 2-
