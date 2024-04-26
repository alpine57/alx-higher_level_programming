#!/usr/bin/python3
"""script takes in a URl request to the URL  displays  value of  X-Request-Id variable found in  header  response"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
