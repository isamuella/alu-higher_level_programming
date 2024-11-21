#!/usr/bin/python3
"""Sends a POST request for an email and displays the response"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    value = requests.post(url, data=email)
    print(value.text)
