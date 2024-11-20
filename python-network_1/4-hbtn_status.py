#!/usr/bin/python3
"""Fetch https://alu-intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    value = requests.get(url)
    status = response.text.strip()

    print("Body response:")
    print("\t- type: {}".format(type(status)))
    print("\t- content: {}".format(status))
