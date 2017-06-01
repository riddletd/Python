#!/usr/bin/python

import os, sys, google

x = raw_input("Starting location: ")
y = raw_input("Destination: ")

google.searchMap(x, y)
