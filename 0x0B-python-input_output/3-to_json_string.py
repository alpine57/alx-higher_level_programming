#!/usr/bin/python3
""" module returns json of  object"""


def to_json_string(my_obj):
    """function that returns JSON rep of an obj"""
    import json

    json_rep = json.dumps(my_obj)
    return json_rep
