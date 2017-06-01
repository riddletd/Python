#!/usr/bin/python

######################################################################
#
# This file is used to store functions for to create, initialize, and
# add all of a directories contents to github. It is also used to
# update the git repository. If you create a new repo, the name will
# be the same as the directory name.
#
# Author: Trevor Riddle
# Creation Date: May 31, 2017
# Update: NULL
#
######################################################################

import os, sys

##
# Creates, initializes, and adds all directory content to the new
# repo. The repo will be the same name as the directory. It also adds
# a README.md file. 
##
def gitinit():
    os.system("curl -u riddletd https://api.github.com/user/repos -d \'{ \"name\": \"" + gitRepoName() + "\" }\'")
    os.system("echo \"# " + gitRepoName() + "\" >> README.md")
    os.system("git init")
    os.system("git add README.md")
    os.system("git commit -m \"first commit\"")
    os.system("git remote add origin https://github.com/riddletd/" + gitRepoName() + ".git")
    os.system("git push -u origin master")
    gitput()

##
# Cleans the directory content of auto-save files, adds them to the
# repo, commit's them with a timestamp, and pushes the content.
##
def gitput():
    os.system("rm *~")
    os.system("rm *#")
    os.system("git add *")
    os.system("git commit -m \"Update: `date +'%Y-%m-%d %H:%M:%S'`\"")
    os.system("git push")

##
# Get's the current directory name to be used to create the new repo.
##
def gitRepoName():
    str = os.path.split(os.getcwd())
    return str[1]
    
    
