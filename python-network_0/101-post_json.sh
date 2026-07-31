#!/bin/bash
# Sends a POST request with the contents of a JSON file and displays the body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
