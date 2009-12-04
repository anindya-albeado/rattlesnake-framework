# -*- coding: utf-8 -*-
"""Job management"""


from core.handlers.exception import JobException, ScriptException
from core.structures.register import Register
from core.structures.counter import Counter


__author__ = "Rattlesnake Team"
__version__ = "1.0"
__package__ = "core.kernel"


class Job:

    job_list = []
    register = Register()
    count_jobid = Counter()

    def __init__(self, runner, name = "Nameless", desc = "NoDesc", \
                 children = None, exc_handler = None):
        # Initialize the attributes of self
        self.id = Job.count_jobid()
        self.runner = runner
        self.exc_handler = exc_handler
        # Set the __name__ attribute of self
        self.__name__ = name
        if self.__name__ == "Nameless" and hasattr(runner, "__name__"):
            self.__name__ = runner.__name__
        self.desc = desc
        if self.desc == "NoDesc" and hasattr(runner, "desc"):
            self.desc = runner.desc
        # Schedule children
        self.children = []
        self.sched(children)
        # Update the job_list adding self to it
        Job.job_list.append(self)
        # Update the register adding self.id to it
        Job.register.extend_availkeys([self.id])

    def __str__(self):
        str = self.__repr__()
        return 'Job > ParentID:%s ID:%s Name:%s' % tuple(str.split("|"))

    def __repr__(self):
        return "%s|%s|%s" % (self.parentid, self.id, self.__name__)


    def __call__(self):
        print str(self)
        self.runner()
        if len(self.children) > 0:
            for child in self.children:
                try:
                    child()
                except JobException as exc:
                    exc_handled = self.exc_handler(exc)
                    if  (exc_handled is True) or (not exc_handled is None):
                        raise exc_handled


    def sched(self, children):
        if not children is None:
            try:
                self.children.extend(children)
            except Exception as exc:
                raise ScriptException(self, str(exc), self.id)

        # Set the parentid to every self.children
        self.set_parentid()

    def set_parentid(self, parentid = None):
        self.parentid = parentid
        if len(self.children) > 0:
            for child in self.children:
                child.set_parentid(self.id)


    def set_regitem(self, value):
        Job.__register.set(self.id, value)

    def get_regitem(self, key):
        """Return a copy of the __register[key]"""

        return Job.__register.get(key)



if __name__ == "__main__":
    print "JobManagement module executed"




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
