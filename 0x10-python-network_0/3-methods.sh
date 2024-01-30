#!/usr/bin/bash
curl -sI -X OPTIONS $1 | grep -i "Allow" | cut -d ":" -f 2- | cut -c 2-
