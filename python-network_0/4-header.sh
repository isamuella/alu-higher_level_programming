#!/bin/bash
# Takes in a URL as an argument, sends a GET request to the URL, and displays the body
curl -s -H "X-HolbertonSchool-User-Id: 98" "http://$1/route_5"
