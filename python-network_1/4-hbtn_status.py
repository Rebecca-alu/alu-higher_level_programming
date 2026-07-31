#!/usr/bin/python3
"""Fetch https://alu-intranet.hbtn.io/status using the urllib package.

This module fetches the status endpoint and displays the raw body
of the response along with its type and its utf-8 decoded content.
"""
import requests


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(r.text)))
        print("\t- content: {}".format(r.text))
