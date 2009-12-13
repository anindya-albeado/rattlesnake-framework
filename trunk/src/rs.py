# -*- coding: utf-8 -*-
"""Client module

Use all of the RattleSnake framework features
"""


# Import client objects
from core.handlers.error import error_fatal_job, error_fatal_script, \
                                error_jobchecker, error_scriptchecker, \
                                error_nonfatal
from core.handlers.IO import msg, messages, warning, warnings, input_exec
from core.structures.counter import Counter
from core.structures.elemchecker import ElemChecker
from core.structures.register import Register
from core.kernel.jobman import Scheduler


__author__ = "Rattlesnake Team"
__version__ = "1.1.0"



if __name__ == "__main__":
    print "RattleSnake client module executed"
