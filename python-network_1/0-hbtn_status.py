#!/usr/bin/python3
"""Fetch https://alu-intranet.hbtn.io/status."""
import urllib.request
from urllib.error import URLError, HTTPError

if __name__ == "__main__":    
    try:
        request = urllib.request.Request("https://alu-intranet.hbtn.io/status")
        with urllib.request.urlopen(request) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode("utf-8")))

    except (HTTPError, UURLError) as e:
        print(f"Error occured: {e}")
        try:
            request = urllib.request.Request("http://0.0.0.0:5050/status")
            with urllib.request.urlopen(request) as response: 
                 body = response.read()
                 print("Body response:")
                 print("\t- type: {}".format(type(body)))
                 print("\t- content: {}".format(body))
                 print("\t- utf8 content: {}".format(body.decode("utf-8")))
    except Exceptio as e:
        print(f"Error ocurred shile fetching secondary URL: {e}")
