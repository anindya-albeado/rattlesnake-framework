# -*- coding: utf-8 -*-
"""Scheduler module"""


from core.kernel.jobman import Job
from core.handlers.exception import RsException, ScriptException, JobException


__author__ = "Rattlesnake Team"
__version__ = "1.0"
__package__ = "core.kernel"


def __init__():
    pass

def add_job(runner, name = "Nameless", desc = "NoDesc", children = None):
    try:
        Job(runner, name, desc, children)
    except ScriptException as exc:
        print exc

def get_jobs():
    return Job.job_list[:]

def run():
    try:
        for job in Job.job_list:
            # Execute only superparent jobs
            if job.parentid is None:
                job()
    except JobException as exc:
        print exc
    except ScriptException as exc:
        print exc
    except RsException as exc:
        print exc

if __name__ == "__main__":
    print "Scheduler module executed"
