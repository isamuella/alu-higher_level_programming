#!/usr/bin/python3
"""
Sends a request to URL and display the value variable in the header
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = requests.get(url)
    print(value.headers.get("X-Request-Id"))
