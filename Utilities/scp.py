#!/usr/bin/env python3

######################################################################
#
# This file will be used to run a secure copy from a remote server.
#
# Author: Trevor Riddle
# Creation Date: June 2, 2017
# Update: -
#
######################################################################

import os, sys, subprocess


server = input("Server: ")
choice = input("\"file\" or \"dir\": ")

source = ""
if choice == "file":
    source = input("File name: ")
elif choice == "dir":
    source = input("Directory name: ")
else:
    print("Not \"file\" or \"dir\"")

dest = input("Destination path: ")

if choice == "file":
    os.system("scp " + server + ":" + source + " " + dest)
else:
    os.system("scp -r " + server + ":" + source + " " + dest)

