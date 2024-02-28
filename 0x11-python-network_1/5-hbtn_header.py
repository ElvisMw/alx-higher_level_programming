#!/usr/bin/python3
"""
Script that takes in a URL, sends a request, and displays the value of the
variable X-Request-Id in the response header using the requests package.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    print(response.headers.get('X-Request-Id', default=None))
