#!/usr/bin/python3
"""creates  function that returns true or false"""


def is_same_class(obj, a_class):
    """function returns True if the object is
    instance ofspecified class else False"""

    if type(obj) is a_class:
        return True
    else:
        return False
