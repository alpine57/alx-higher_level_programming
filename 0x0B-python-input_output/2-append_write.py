#!/usr/bin/python3
"""appends string to end of  file"""

def append_write(filename="", text=""):
    """adds text to the end of filename and returns  characters  added"""
    with open(filename, 'a') as file:
        file.write(text)
        return(len(text))
