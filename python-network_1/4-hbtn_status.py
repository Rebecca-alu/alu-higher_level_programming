#!/usr/bin/python3
"""Fetch https://alu-intranet.hbtn.io/status using the urllib package.

This module fetches the status endpoint and displays the raw body
of the response along with its type and its utf-8 decoded content.
"""
import urllib.request


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
