#!/usr/bin/python3
"""Use the GitHub API to display your id from my GitHub credentials"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    auther = (username, password)
    try:
        value = requests.get(url, auth=auther)
        value.raise_for_status()
        print(value.json().get("id"))
    except requests.exceptions.RequestException:
        print("None")
