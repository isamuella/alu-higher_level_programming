#!/usr/bin/python3
"""Fetch https://intranet.hbtn.io/status."""
import urllib.request


if __name__ == "__main__":
    try:
        # Attempt to access the first URL
        request = urllib.request.Request("https://intranet.hbtn.io/status")
        with urllib.request.urlopen(request) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode("utf-8")))

    except urllib.error.HTTPError as e:
        # Handle the case where the HTTP error occurs
        print(f"HTTPError: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        # If URLError occurs, it may indicate a connection issue
        print(f"URLError: {e.reason}")
    except Exception as e:
        # Catch other unforeseen exceptions
        print(f"Unexpected error: {str(e)}")
        
    # Fallback to another URL if the above fails
    try:
        request = urllib.request.Request("http://0.0.0.0:5050/status")
        with urllib.request.urlopen(request) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode("utf-8")))
    except Exception as e:
        print(f"Failed to fetch fallback URL: {str(e)}")
