#!/usr/bin/python3
"""Sends a letter to the search_user API and displays the result"""
import requests
import sys


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": letter})
    try:
        j = r.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if not j:
            print("No result")
        else:
            print("[{}] {}".format(j.get("id"), j.get("name")))
