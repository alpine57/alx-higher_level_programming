#!/usr/bin/python3
"""module add attributes to objects."""


def add_attribute(obj, att, value):
    """define  function  adding  new attribute to  object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
