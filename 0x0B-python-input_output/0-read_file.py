#!/usr/bin/python3
"""reads a UTF8 text file and prints it to stdout"""

def read_file(filename=""):
    """reads file and prints  to stdout"""
    with open(filename,  encoding="utf-8") as file:
        read = file.read()
        print(read, end="")
