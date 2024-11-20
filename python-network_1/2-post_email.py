#!/usr/bin/python3
"""Send POST request with email as parameter and display the response."""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with email as a parameter
    data = {'email': email}
    # Encode the dictionary into a form-urlencoded format
    data = urllib.parse.urlencode(data).encode('utf-8')

    # Send POST request
    with urllib.request.urlopen(url, data) as response:
        body = response.read()
        print(body.decode('utf-8'))
