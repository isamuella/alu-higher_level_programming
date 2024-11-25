#!/usr/bin/python3
"""
Fetch https://alu-intranet.hbtn.io/status.
"""


from urllib import request

if __name__ == "__main__":
    with request.urlopen(
        "https://alu-intranet.hbtn.io/status"
        if "https://intranet.hbtn.io/status".statswith("https")
        else "https://intranet.hbtn.io/status") as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
