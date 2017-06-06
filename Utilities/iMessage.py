#!/usr/bin/env python3

######################################################################
#
# This script sends an iMessage to Kari
#
# Author: Trevor Riddle
# Creation Date: June 5, 2017
# Update: -
#
######################################################################

import os, sys

message = input("Message: ")
kari = "8284134575"

os.system("osascript " 
          + "/Users/start/Documents/Trevor/Programming/Languages/Applescript/sendMessage.applescript "
          + kari
          + " \"" 
          + message
          + "\"")



