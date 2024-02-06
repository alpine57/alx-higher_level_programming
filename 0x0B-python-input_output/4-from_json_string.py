#!/usr/bin/python3
""" module that treturns an object rep of json"""

def from_json_string(my_str):
    """function that returns  obj rep of JSON"""
    import json

    json_rep = json.loads(my_str)
    return (json_rep)
