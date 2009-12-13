# -*- coding: utf-8 -*-
"""Job management"""


from core.handlers.exception import JobException, ScriptException, \
                                    RsException
from core.structures.register import Register
from core.structures.counter import Counter
from core.structures.doubledict import DoubleDict


__author__ = "Rattlesnake Team"
__version__ = "1.0"
__package__ = "core.kernel"


class Scheduler:
    def __init__(self):
        self.h_j = DoubleDict()
        # root_job initializing
        self.root_job = Job(self.__root_runner, "Root", "Parent of all jobs")
        h = Handler()
        self.h_j.set_obj2(h, self.root_job)
        self.h_j.set_obj1(self.root_job, h)

    def add_job(self, runner, name = "Nameless", desc = "NoDesc", \
                parent = None, exc_handler = None):
        try:
            if parent is None:
                parent = self.h_j.obj1_lookup(self.root_job)
            j = Job(runner, name, desc, exc_handler = exc_handler)
            h = Handler()
            # Set the dict { Handlers : Jobs }
            self.h_j.set_obj2(h, j)
            # Set the dict { Jobs : Handlers }
            self.h_j.set_obj1(j, h)
            # Set to the parent the 'j' Job as a child
            parent_job = self.h_j.obj2_lookup(parent)
            parent_job.sched([j])
        except ScriptException as exc:
            print exc
        # Return the handler to the caller
        return h

    def run(self):
        try:
            self.root_job(self.h_j)
        except JobException as exc:
            print exc
        except ScriptException as exc:
            print exc
        except RsException as exc:
            print exc

    def set_regitem(self, handler, value):
        j = self.h_j.obj2_lookup(handler)
        j.set_regitem(j, value)

    def get_regitem(self, handler):
        j = self.h_j.obj2_lookup(handler)
        j.get_regitem(j.id)

    def __root_runner(self):
        pass

class Handler:

    def __init__(self):
        self.onstart_job_exec = None
        self.onstop_job_exec = None
        self.onstart_children_exec = None
        self.onstop_children_exec = None
        self.onstart_child_exec = None
        self.onstop_child_exec = None


    def onstart_job(self):
        if not self.onstart_job_exec is None:
            try:
                for task in self.onstart_job_exec:
                    task()
            except TypeError:
                self.onstart_job_exec()
    def onstop_job(self):
        if not self.onstop_job_exec is None:
            try:
                for task in self.onstop_job_exec:
                    task()
            except TypeError:
                self.onstop_job_exec()
    def onstart_children(self):
        if not self.onstart_children_exec is None:
            try:
                for task in self.onstart_children_exec:
                    task()
            except TypeError:
                self.onstart_children_exec()
    def onstop_children(self):
        if not self.onstop_children_exec is None:
            try:
                for task in self.onstop_children_exec:
                    task()
            except TypeError:
                self.onstop_children_exec()
    def onstart_child(self):
        if not self.onstart_child_exec is None:
            try:
                for task in self.onstart_child_exec:
                    task()
            except TypeError:
                self.onstart_child_exec()
    def onstop_child(self):
        if not self.onstop_child_exec is None:
            try:
                for task in self.onstop_child_exec:
                    task()
            except TypeError:
                self.onstop_child_exec()


class Job:

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
        # Update the register adding self.id to it
        Job.register.extend_availkeys([self.id])

    def __str__(self):
        str = self.__repr__()
        return 'Job > ParentID:%s ID:%s Name:%s' % tuple(str.split("|"))

    def __repr__(self):
        return "%s|%s|%s" % (self.parentid, self.id, self.__name__)


    def __call__(self, h_j):
        print str(self)
        # Get the handler linked to the 'self' job
        handler = h_j.obj1_lookup(self)
        # onstart_job event
        handler.onstart_job()
        self.runner()
        if len(self.children) > 0:
            # onstart_children event
            handler.onstart_children()
            for child in self.children:
                try:
                    # onstart_child event
                    handler.onstart_child()
                    child(h_j)
                    # onstop_child event
                    handler.onstop_child()
                except JobException as exc:
                    exc_handled = self.exc_handler(exc)
                    if  (exc_handled is True) or (not exc_handled is None):
                        raise exc_handled
            # onstop_children event
            handler.onstop_children()
        # onstop_job event
        handler.onstop_job()


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

    def get_regitem(self, id_job):
        """Return a copy of the __register[key]"""

        return Job.__register.get(id_job)



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
