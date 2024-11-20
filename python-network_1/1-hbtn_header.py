#!/usr/bin/python3
"""Takes in a  URL and display the X-Request-Id header variable."""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
