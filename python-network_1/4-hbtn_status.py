#!/usr/bin/python3
"""Fetch https://alu-intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    value = requests.get(url)
    body = value.text

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
