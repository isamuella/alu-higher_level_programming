#!/usr/bin/python3
"""Fetch https://alu-intranet.hbtn.io/status."""

import requests


if __name__ == "__main__":
    value = requests.get( "https://alu-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(value.text)))
    print("\t- content: {}".format(value.text))
