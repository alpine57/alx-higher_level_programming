#!/usr/bin/python3
""" Int class """


class MyInt(int):
    """defines  class that connverts == !=. operators """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
