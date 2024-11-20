#!/usr/bin/python3
"""
Module to fetch and display the response from https://alu-intranet.hbtn.io/status
"""
from urllib.request import urlopen, Request


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    # Add a User-Agent header to the request
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    
    with urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
