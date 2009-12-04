# -*- coding: utf-8 -*-
"""Exceptions implementation

Users shouldn't directly call exceptions, but errors in the Error module.
"""


__author__ = "Rattlesnake Team"
__version__ = "1.0"
__package__ = "core.handlers"


class RsException(Exception):
    """General Rattlesnake exception
    
    Used by other Rattlesnake exceptions
    """

    def __init__(self, unitName, reason):
        self.unitName = unitName
        self.reason = reason


    def __str__(self):
        return "Exception caused by: %s. Reason: %s" % (self.unitName, \
                                                        self.reason)

    def __repr__(self):
        return "%s,%s" % (self.unitName, self.reason)


class JobException(RsException):
    """Job level exception
    
    Stop the job execution
    """

    def __init__(self, unitName, reason, id_job = None):
        RsException.__init__(self, unitName, reason)
        self.id_job = id_job


    def __str__(self):
        return "Job: %s (%s) is aborted. Reason: %s" % \
                (self.id_job, self.unitName, self.reason)

    def __repr__(self):
        return "%s|%s|%s" % (self.id_job, self.unitName, self.reason)

class ScriptException(RsException):
    """Script level exception
    
    Stop the script execution
    """

    def __init__(self, unitName, reason, id_job = None):
        RsException.__init__(self, unitName, reason, id_job)


    def __str__(self):
        string = "The script is aborted. Cause: Job > "
        if not self.id_job is None:
            string += self.id_job + " - "
        string += "%s. Reason: %s" % (self.unitName, self.reason)
        return string

    def __repr__(self):
        return "%s,%s%,s" % (self.id_job, self.unitName, self.reason)


class RegisterException (RsException):
    """Register structure exception
    
    Stop the script execution
    """
    def __init__(self, key):
        RsException.__init__(key, """It's not available, because it
                                  doesn't correspond to any scheduled jobs""")


    def __str__(self):
        return "Error with Key: %s. Reason %s" % (self.unitName, \
                                                  self.reason)

    def __repr__(self):
        return RsException.__repr__(self)



if __name__ == "__main__":
    print "Exception module executed"




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
