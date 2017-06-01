#!/usr/bin/python

######################################################################
#
# This Python code will do a youtube search
#
# Author: Trevor Riddle
# Creation Date: -
# Update: -
#
######################################################################

import os, sys, google

url = "https://www.youtube.com/results?search_query="
search = raw_input("Search: ")
plusSearch = google.plusSep(search)

os.system("open " + url + plusSearch)

