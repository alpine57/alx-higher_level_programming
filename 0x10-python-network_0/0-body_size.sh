#!/bin/bash
#Sends request to URL, and displays the size of  body
curl -s $1 | wc -c
