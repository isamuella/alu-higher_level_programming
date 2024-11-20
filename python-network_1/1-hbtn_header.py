#!/usr/bin/python3
"""Fetch URL and display the X-Request-Id header value."""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        # Extract and print the X-Request-Id header value
        print(response.headers.get('X-Request-Id'))
