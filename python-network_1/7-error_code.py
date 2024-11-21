#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = requests.get(url)

    if value.status_code >= 400:
        print("Error code: {}".format(value.status_code))

    else:
        print(value.text)
