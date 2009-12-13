# -*- coding: utf-8 -*-
"""ElemChecker structure"""


import re
from core.handlers.exception import RsException


__author__ = "Rattlesnake Team"
__version__ = "1.1.0"
__package__ = "core.structures"


class ElemChecker:
    def __init__(self, matcher):
        self.matcher = matcher


    def __call__(self, elem):
        founds = []
        try:
            for matcher_key, matcher_value in self.matcher.items():
                try:
                    for value in matcher_value:
                        # Dict of iterable elements
                        if value == elem:
                            founds.append(matcher_key)
                            break
                except:
                    # Dict of non-iterable elements
                    try:
                        matcher_value = re.compile(matcher_value)
                        comparison_result = re.match(matcher_value, elem)
                        if not comparison_result is None:
                            founds.append(matcher_key)
                    except TypeError:
                        raise RsException("ElemChecker", \
                                          "cannot use %s as a regex string")
        except TypeError:
            raise RsException("ElemChecker", "%s isn't iterable" % \
                              (self.matcher,))



if __name__ == "__main__":
    print "ElemChecker module executed"




# This file is part of the Rattlesnake project.
#
# Rattlesnake is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License 3 as published by
# the Free Software Foundation.
#
# Rattlesnake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# Copyright (C) 2009 Rattlesnake Team - All rights reserved.
