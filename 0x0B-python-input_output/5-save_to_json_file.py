#!/usr/bin/python3
""" module usthat es json rep to write  files"""

def save_to_json_file(my_obj, filename):
    """object to  text file using json rep"""
    import json

    with open(filename, "w") as file:
        json.dump(my_obj, file)

