#!/usr/bin/python3
"""Fetch https://intranet.hbtn.io/status."""
from urllib.request import urlopen


if __name__ == "__main__":    
    try:
        url = "https://intranet.hbtn.io/status"
        with urlopen(url) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode("utf-8")))

    except:
        url = "https://intranet.hbtn.io/status"
        with urlopen(url) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode("utf-8")))
