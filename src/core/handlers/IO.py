# -*- coding: utf-8 -*-
"""Input/Output handler"""


from core.structures.elemchecker import ElemChecker


__author__ = "Rattlesnake Team"
__version__ = "1.1.0"
__package__ = "core.handlers"

messages = []
warnings = []


def warning(unitName, reason):
    """A warning is occurred
    
    Behaviour:
    1- Print the warning
    2- Register the warning to the warnings list
    """

    global warnings
    warnings.append((unitName, reason))
    print "Warning -- %s: %s" % (unitName, reason)

def msg(message, unitName = None):
    """Message print
    
    Behaviour:
    1- Print the message
    2- Register the message to the messages list
    """

    global messages
    messages.append((unitName, message))
    str = ""
    if not unitName is None:
        str = "%s: " % (unitName,)
    str += "%s" % (message,)
    print str


def input_exec(yes_function, no_function, pre_msg = "", \
               question = "Do you want to continue? [y,n]\t", \
               checker = ElemChecker({"yes":["yes", "y"], "no":["no", "n"]})):
    """Execute a function based to the user input.
    
    Keyword arguments:
    - yes_function: Function executed only if the input is a 'yes' input
    - no_function: Function executed only if the input is a 'no' input
    - pre_msg: Cause of the input_exec
    - question: Question asked for getting the input
    - checker: ElemChecker object. It can be:
             - {'yes':['allowed_yes_input', ..], 'no':['allowed_no_input', ..]}
             - {'yes':'yes_regex_string, 'no':'no_regex_string'}
    
    
    Behaviour:
    1- Print pre_msg - The cause of the call of this method
    2- Print question - Message shown to the user for getting the desidered
       input
    3- If the input is in the 'yes' list it executes the true_function,
       else if it's in the 'no' list it executes the false_function
    """

    input = ""
    if pre_msg is not "": msg(input_exec, pre_msg)
    # Get the input and execute the correlated function
    while not checker(input):
        input = raw_input(question)
        # Get the input and check if it's a 'yes' or 'no' input
        founds = checker(input)
        if "yes" in founds:
            if callable(yes_function):
                yes_function()
            else:
                warning("The function %s isn't callable" % (yes_function,))
        elif "no" in founds:
            if callable(no_function):
                no_function()
            else:
                warning("The function %s isn't callable" % (no_function,))



if __name__ == "__main__":
    print "Input/Output module executed"



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
