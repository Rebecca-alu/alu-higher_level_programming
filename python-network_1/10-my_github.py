#!/usr/bin/python3
"""Displays the GitHub id of the authenticated user"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    r = requests.get("https://api.github.com/user", auth=(username, password))
    print(r.json().get("id"))
