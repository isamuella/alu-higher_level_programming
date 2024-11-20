#!/usr/bin/python3
"""Fetch https://alu-intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    value = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(value.text)))
    print("\t- content: {}".format(value.text))
