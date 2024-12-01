#!/usr/bin/python3
"""Fetch  the https://alu-intranet.hbtn.io/status"""

import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    if url.startswith('https://'):
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
