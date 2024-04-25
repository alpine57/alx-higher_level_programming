#!/bin/bash
# Display all HTTP methods  server to  give URL will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
