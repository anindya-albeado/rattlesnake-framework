# -*- coding: utf-8 -*-
"""General test module"""


from core.kernel.jobman import Job
from core.handlers.exception import ParentException

__author__ = "Rattlesnake Team"
__version__ = "1.0"
__package__ = "samples"


class t_one:
    def __init__(self):
        print ">>\tt_one object initialized"
    def __call__(self):
        print ">>\tt_one object called"
    def m_one(self):
        print ">>\tm_one method of t_one object called"
    def m_two(self):
        print ">>\tm_two method of t_one called"

class t_two:
    def __init__(self):
        print ">>\tt_two object initialized"
    def __call__(self):
        print ">>\tt_two object called"
    def m_one(self):
        print ">>\tm_one method of t_two object called"
    def m_two(self):
        print ">>\tm_two method of t_two object called"
    def m_three(self):
        print ">>\tm_three method of t_two object called"

def t_three():
    print ">>\tt_three method called"

def t_four():
    print ">>\tt_four method called"

def t_big():
    print ">>\tt_big method called"

if __name__ == "__main__":
    tone = t_one()
    ttwo = t_two()
    # Job structure:
    # 
    # Job job_big    ------->    t_big
    #
    #                   |-------> Job jtone      ------->    tone
    #                       |-------> Job m_one      ------->    m_one
    #                       |-------> Job m_two      ------->    m_two
    #
    #                   |-------> Job jttwo      ------->    ttwo
    #                       |-------> Job m_one      ------->    m_one
    #                       |-------> Job m_two      ------->    m_two
    #                       |-------> Job m_three    ------->    m_three
    #
    #                   |-------> Job jtthree    ------->    t_three
    #
    #
    # Job jtfour     ------->    t_four
    #

    j1 = Job(tone.m_one, "Job1.1", desc = "method one of test one")
    j2 = Job(tone.m_two, "Job1.2", desc = "method two of test one")
    jttwo = Job(ttwo, "Job2", "test two object",
                [Job(ttwo.m_one, "Job2.1", "method one of test two"), \
                 Job(ttwo.m_two, "Job2.2", "method two of test two", \
                   [Job(ttwo.m_three, "Job2.3", "method three of test two", \
                        [Job(t_three, "Job2.3.1", "test three method")])])])

    jtone = Job(tone, "Job1", desc = "test one object", children = [j1, j2])
    #jtthree = Job(t_three, desc = "test three method")
    #jtfour = Job(t_four, desc = "test four method")
    job_big = Job(t_big, "JobBig", "test big method", [jtone, jttwo])
    #job_big.sched([jtthree])
    job_big()
    #jtfour()
    print "JobList:\t%s" % (Job.job_list,)
    print "Register:\t%s" % (Job.register.get_availkeys(),)


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
