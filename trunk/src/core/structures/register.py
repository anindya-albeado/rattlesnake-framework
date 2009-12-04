# -*- coding: utf-8 -*-
"""Register structures"""


from copy import copy
from core.handlers.exception import RegisterException


__author__ = "Rattlesnake Team"
__version__ = "1.0"
__package__ = "core.structures"


class Register:
    """Dict of lists with an esclusive set item based on available keys"""

    def __init__(self, keys = []):
        self.__avail_keys = list(keys)
        self.__dict = dict((key, [None, ]) for key in self.__avail_keys)


    def set(self, key, value):
        """Append at key list the value only if key is in available_keys"""

        if key in self.__avail_keys:
            if self.__dict[key][0] is None:
                self.__dict[key] = [value, ]
            else:
                self.__dict[key].append(value)
        else:
            raise RegisterException(key)

    def get(self, key):
        """Get the key list"""

        if key in self.__dict.keys():
            return copy(self.__dict[key])
        else:
            raise RegisterException(key)


    def extend_availkeys(self, keys):
        """Extend the available keys with the keys list"""

        self.__avail_keys.extend(keys)

    def get_availkeys(self):
        return self.__avail_keys[:]



if __name__ == "__main__":
    print "Register module executed"




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
