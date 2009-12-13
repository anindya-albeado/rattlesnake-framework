# -*- coding: utf-8 -*-
"""Counter structures

Generate an unique id
"""


__author__ = "Rattlesnake Team"
__version__ = "1.1.0"
__package__ = "core.structures"


class Counter:
    """Generate unique id"""

    def __init__(self):
        self.__id = 0
        self.step = 1

    def __call__(self):
        """ Generate and return a unique id
        
        Behaviour:
        1- Increment the id with the step
        2- Return the incremented id
        """

        self.__id += self.step
        return self.__id


if __name__ == "__main__":
    print "Counter module executed"




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
