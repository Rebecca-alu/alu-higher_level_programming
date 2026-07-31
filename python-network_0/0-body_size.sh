#!/usr/bin/env bash
# Displays the size (in bytes) of the body of the response for a given URL
curl -s -o /dev/null -w "%{size_download}\n" "$1"
