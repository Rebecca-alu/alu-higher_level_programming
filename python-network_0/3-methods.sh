#!/usr/bin/env bash
# Displays all HTTP methods the server will accept for the given URL
curl -s -X OPTIONS -i "$1" | grep -i "Allow:" | cut -d " " -f 2-
