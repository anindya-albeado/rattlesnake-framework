# -*- coding: utf-8 -*-
"""New features module tester"""


import rs


__author__ = "Rattlesnake Team"
__version__ = "1.0"
__package__ = "samples"


class test_one:
    def __init__(self):
        print "test_one object initialized"
    def __call__(self):
        print "test_one object called"
    def m_one(self):
        print "m_one method of test_one called"
    def m_two(self):
        print "m_two method of test_one called"
class test_two:
    def __init__(self):
        print "test_two object initialized"
    def __call__(self):
        print "test_two object called"
    def m_one(self):
        print "m_one method of test_two called"
    def m_two(self):
        print "m_two method of test_two called"
    def m_three(self):
        print "m_three method of test_two called"

def test_four():
    print "test_four method called"



if __name__ == "__main__":
    t_one = test_one()
    t_two = test_two()

    # Using the Rattlesnake Framework

    sched_one = rs.Scheduler()
    h_t_one = sched_one.add_job(t_one)
    h_m_one_t_one = sched_one.add_job(t_one.m_one, parent = h_t_one)
    h_m_two_t_one = sched_one.add_job(t_one.m_two, parent = h_m_one_t_one)
    h_t_two = sched_one.add_job(t_two)
    h_m_one_t_two = sched_one.add_job(t_two.m_one, parent = h_t_two)
    h_m_two_t_two = sched_one.add_job(t_two.m_two, parent = h_m_one_t_two)

    sched_one.run()




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
