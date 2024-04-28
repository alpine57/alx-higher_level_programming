#!/bin/bash
# Send JSON POST request to given URL with JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
