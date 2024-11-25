#!/bin/bash
# Takes in a URL as an argument, sends a GET request to the URL, and displays the body
curl -sH "X-HolbertonSchool-User-Id: 98" -o response body.txt "$1" && cat response_body.txt
