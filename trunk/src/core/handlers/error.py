# -*- coding: utf-8 -*-
"""Errors handlers

Users should call them instead of exceptions
"""


from core.handlers.exception import ScriptException, JobException, RsException, \
    RegisterException
from core.handlers.IO import warning


__author__ = "Rattlesnake Team"
__version__ = "1.1.0"
__package__ = "core.handlers"

errors_fatal = {"job":[], "script":[]}
errors_nonfatal = []


def error_fatal_script(unitName, reason):
    """Error fatal for the script
    
    Break the script execution.
    Register the infos about the error in the errors_fatal["script"] list
    """

    global errors_fatal
    errors_fatal["script"].append((unitName, reason))
    print """%s raised the following error: %s. The script execution is 
          terminated""" % (unitName, reason)
    raise ScriptException(unitName, reason)

def error_fatal_job(unitName, reason):
    """Error fatal for the job
    
    Break the job execution.
    Register the infos about the error in the errors_fatal["job"] list
    """

    global errors_fatal
    errors_fatal["job"].append((unitName, reason))
    print """%s raised the following error: %s. %s execution is terminated but
          the script execution will continue""" % (unitName, reason, unitName)
    raise JobException(unitName, reason)


def error_scriptchecker(unitName, reason):
    """Script error with input checking
    
    Check if input is a 'yes' or 'no' input.
    If it is a 'yes' input it raises a error_fatal_script
    If it is a 'no' input it raises a error_fatal_job
    """

    input = ""
    yes = set(("yes", "y"))
    no = set(("no", "n"))
    admitted = yes & no
    while not input.lower() in admitted:
        input = raw_input("Do you want to continue? [y,n]\t")
        if input in yes:
            # The caller input is a 'yes' input
            error_fatal_job(unitName, reason)
        elif input in no:
            # The caller input is a 'no' input
            error_fatal_script(unitName, reason)

def error_jobchecker(unitName, reason):
    """Job error with input checking

    If it is a 'yes' input it raises a error_fatal_job
    If it is a 'no' input it call a error_nonfatal
    """

    input = ""
    yes = set(("yes", "y"))
    no = set(("no", "n"))
    admitted = yes & no
    while not input.lower() in admitted:
        input = raw_input("Do you want to continue? [y,n]\t")
        if input in yes:
            error_nonfatal(unitName, reason)
        elif input in no:
            error_fatal_job(unitName, reason)


def error_nonfatal(unitName, reason):
    """
    Register that a error is occurred in the errors_nonfatal list
    """

    global errors_nonfatal
    errors_nonfatal['job'].append((unitName, reason))
    warning("The Job execution will continue", unitName)



if __name__ == "__main__":
    print "Error module executed"




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
