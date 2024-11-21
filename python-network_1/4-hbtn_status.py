#!/usr/bin/python3
"""Fetch status from a URL and display the content."""

import requests


if __name__ == "__main__":
    # Define both URLs for testing purposes
    url = "https://alu-intranet.hbtn.io/status"  # For the production test
    fallback_url = "http://0.0.0.0:5050/status"  # For the local test
    
    # Fetch content from the production URL first
    try:
        value = requests.get(url)
        value.raise_for_status()  # Raise error if the request fails
    except requests.exceptions.RequestException:
        # If the production URL fails, fallback to the local URL
        value = requests.get(fallback_url)

    # Extract and print the response body
    body = value.text

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
