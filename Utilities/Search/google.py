#!/usr/bin/python

######################################################################
#
# This code is used to search google maps for a string specified on
# stdin. The goal is to change an input string where the words are
# separated by spaces into a string where the words are separated with
# +'s. This is the standard separator for the google maps url.
#
######################################################################

import os, sys

##
# Searches google maps based on a starting location and a destination.
##
def searchMap(start, dest):
    s = plusSep(start)
    d = plusSep(dest)
    os.system("open https://www.google.com/maps/dir/" + s + "/" + d)

##
# Does a google search.
##
def searchGoogle(search):
    os.system("open https://www.google.com/#q=" + plusSep(search))

##
# Replaces a whitespace (' ') separated string with a plus ('+')
# separated string.
##
def plusSep(str):
    tmp = "";
    for c in str:
        if c == ' ': tmp += "+"
        else: tmp += c
    return tmp
