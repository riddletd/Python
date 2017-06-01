#!/usr/bin/env python3

######################################################################
#
# This is a utility to "clean" the files whenever the "ls" command is 
# called.
#
# Author: Trevor Riddle
# Creation Date: -
# Update: -
#
######################################################################

import os, sys

os.system("rm *~ >/dev/null 2>&1")
os.system("rm *# >/dev/null 2>&1")
os.system("ls")
