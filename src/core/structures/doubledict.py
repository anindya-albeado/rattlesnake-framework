# -*- coding: utf-8 -*-
"""Doubledict module"""


__author__ = "Rattlesnake Team"
__version__ = "1.0"
__type__ = "core.structures"


class DoubleDict():

    def __init__(self):
        # obj1 is key. obj2 is value
        self.obj1_obj2 = {}
        # obj2 is key. obj1 is value
        self.obj2_obj1 = {}


    def obj1_lookup(self, obj2):
        """Return the obj1 linked to the passed obj2"""
        return self.obj2_obj1[obj2]

    def obj2_lookup(self, obj1):
        """Return the obj2 linked to the passed obj1"""
        return self.obj1_obj2[obj1]


    def set_obj1(self, obj2, obj1):
        """Link to the obj2 key the obj1 value"""
        self.obj2_obj1[obj2] = obj1

    def set_obj2(self, obj1, obj2):
        """Link to the obj1 key the obj2 value"""
        self.obj1_obj2[obj1] = obj2

if __name__ == "__main__":
    print "module executed"
