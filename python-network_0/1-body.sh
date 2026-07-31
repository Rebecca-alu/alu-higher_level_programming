#!/bin/bash
# Sends a GET request and displays the body, only if status code is 200
curl -s -o /tmp/body_output -w "%{http_code}" "$1" > /tmp/body_status
if [ "$(cat /tmp/body_status)" = "200" ]; then
    cat /tmp/body_output
fi
