#!/usr/bin/python3
"""Sends a POST request with the letter as a parameter"""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    letter = {"q": q}

    value = requests.post(url, data=letter)
    try:
        response = value.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
