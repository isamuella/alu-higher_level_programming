#!/bin/bash
# Takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sL "$1" -w "%{http_code}" -o temp_response.txt | grep -q '200' && cat temp_response.txt
