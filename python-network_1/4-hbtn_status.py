#!/usr/bin/python3
"""Fetch https://alu-intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
   try:
       url = "https://alu-intranet.hbtn.io/status"
       value = requests.get(url)
       value.raise_for_status()
   except requests.exceptions.RequestException:
       url = "http://0.0.0.0:5050/status"
       value = requests.get(url)

       status = value.text.strip()

    print("Body response:")
    print("\t- type: {}".format(type(status)))
    print("\t- content: {}".format(status))
