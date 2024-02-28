#!/usr/bin/python3
"""
Takes in a URL, sends a request, and displays the body of the response
Handles urllib.error.HTTPError exceptions and prints he HTTP
status code on error.
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
