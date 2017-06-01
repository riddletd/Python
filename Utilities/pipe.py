#!/usr/bin/env python3

######################################################################
#
# This utility program reads in a file that puts a pipe between each
# program. You can use this to write a file consisting of multiple
# utility programs that you know you want to pipe together and this
# program will put in all of the pipes and run the program for you.
#
# Author: Trevor Riddle
# Creation Date: May 31, 2017
# Update: -
#
######################################################################

import os, sys

output = ""

def pipeInFile(str):
    if os.path.isfile(str):
        file = open(str, "r")
        output = pipeSep(file.read())
    else: print("Not a file")
        

def pipeSep(str):
    tmp = ""
    count = 0
    
    # Puts a pipe "|" between every command unless it has a numeric
    # value after it. If it does, then the pipe is place after all
    # numeric input values.
    for c in str:
        if (c.isdigit()): tmp += c
        elif (c == ' ' and not str[count + 1].isdigit()): tmp += " | " 
        else: tmp += c
        count += 1
    print(tmp)
    return tmp

pipeInFile(sys.argv[1])
print(output)
