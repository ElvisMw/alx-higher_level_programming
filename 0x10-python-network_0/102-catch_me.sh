#!/bin/bash
curl -sLX PUT "$1/catch_me" -d "user_id=98" -H "Origin: HolbertonSchool"
