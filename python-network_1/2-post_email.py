#!/usr/bin/python3
"""Takes in a URL and sends a POST email request and display the response."""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}

    data = urllib.parse.urlencode(data).encode('utf-8')

    # Sending a POST request
    with urllib.request.urlopen(url, data) as response:
        body = response.read()
        print(body.decode('utf-8'))
