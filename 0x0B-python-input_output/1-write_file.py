#!/usr/bin/python3
"""writes to a text file returns number of characters writen"""

def write_file(filename="", text=""):
    """ write number of text written"""
    with open(filename,  'w') as file:
        word = file.write(text)
        return word
