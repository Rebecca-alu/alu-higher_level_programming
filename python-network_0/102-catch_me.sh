#!/bin/bash
# Send a spoofed request that tricks the server into believing user_id is 98
curl -s -L -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" "0.0.0.0:5000/catch_me"
