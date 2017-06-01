#!/usr/bin/env python3

######################################################################
#
# Takes a sequence of words and orms them into a list of words where
# each word is set on a new line.
#
# Author: Trevor Riddle
# Creation Date: June 1, 2017
# Update: -
#
######################################################################

import os, sys

file = sys.argv[1]

##
# If the input is a file, cmdline args, or a string, all words in the 
# input are put on a newline.
##
def list(file):
    if os.path.isfile(file):
        f = open(file)
        list = f.read().split(" ")
        for x in list:
            print(x)
    else:
        for word in sys.argv:
            if sys.argv[0] == word: continue
            elif " " in word: 
                list = word.split(" ")
                for x in list:
                    print(x)
            else:
                print(word)

list(file)
