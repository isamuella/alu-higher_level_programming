#!/bin/bash
# Takes in a URL as an argument, sends a GET request to the URL, and displays the body
curl -sH "X-HolbertonSchool-User-Id: 98" "$1" -X GET
