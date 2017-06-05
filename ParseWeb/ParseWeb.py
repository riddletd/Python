#!/usr/bin/env python3

######################################################################
#
# This code is used to get a Tutorial's Point tutorial and format it
# using LaTeX. I am creating this to be able to quickly print a
# tutorial without having to pay for the $9.99 pdf copy charge.
#
# I will be able to get the tutorials content be parsing the web page
# and saving the header and paragraph content to a file. Then I will
# parse the header and paragraph content file and replace the tags
# with LaTeX tags.
#
# Author: Trevor Riddle
# Creation Date: June 5, 2017
# Update: -
#
######################################################################

import os, sys, requests, re


##
# Replace spaces in a string with underscores.
##
def underscoreSep(str):
    tmp = "";
    for c in str:
        if c == ' ': tmp += "_"
        else: tmp += c
    return tmp

##
# Gets a requested tutorial from Tutorials Point and saves the html
# content to a file. 
##
def getTutorial(ext):
    
    # Add the specific extension for tutorial page
    tutorial = tp_url + ext[1:-1]
    print(tutorial)
    html = requests.get(tutorial)
    str = html.text

    # Get Title of page
    search = re.search(r'<title>.*</title>', str)
    htmlContent.write(search.group() + "\n\n")

    # Get headers and paragraphs of page
    para = re.findall(r'<h\d.*>.*</h\d>|<p>.*</p>', str)
    for x in para:
        htmlContent.write(x + "\n\n")
    
    pre = re.findall(r'<pre.*>.*</pre>', str, re.DOTALL)
    for x in pre:
        htmlContent.write(x + "\n\n")

    

##
# Gets a list of tutorial page extensions from Tutorials Point
##
def getList(url):
    html = requests.get(url + tut_ext + "/index.htm")
    str = html.text

    para = re.findall(r'<li><a.*>.*</a></li>', str)
    htmlList = open(tut_ext + ".tut.list", "a+")
    for x in para:
        tmp = re.sub(r'<li><a.*href="', "", x)
        ext = re.sub(r'".*', "", tmp)
        htmlList.write(ext + "\n")
        
    htmlList.close()
    
    f = open(tut_ext + ".tut.list", "r")
    lines = f.readlines()
    f.close()

    f = open(tut_ext + ".tut.list2", "a+")
    for line in lines:
        if line.startswith("/" + tut_ext + "/"):
            f.write(line)
        else: continue
    
    f.close()

##
# Convert to LaTeX syntax
##
def latex(str):
    
    if str.find("html") != -1:
        str = re.sub(r'<.*html>', "", str)
        str = re.sub(r'</html>', "", str)
        latexContent.write(str)

    elif str.find("body") != -1:
        str = re.sub(r'<body>', "", str)
        str = re.sub(r'</body>', "", str)
        latexContent.write(str)

    elif str.find("<title>") != -1:
        str = re.sub(r'<title>', r"\title{", str)
        str = re.sub(r'</title>', "}", str)
        latexContent.write(str)

    elif str.find("<h") != -1:
        str = re.sub(r'<h\d.*>', r"\lhead{", str)
        str = re.sub(r'</h\d>', "}", str)
        latexContent.write(str)

    elif str.find("<p>") != -1:
        str = re.sub(r'<p>', r"\begin{flushleft}", str)
        str = re.sub(r'</p>', r"\end{flushleft}", str)
        latexContent.write(str)

    elif str.find("<pre") != -1:
        str = re.sub(r'<pre.*>', r"\begin{lstlisting}", str)
        str = re.sub(r'</pre>', r"\end{lstlisting}", str)
        latexContent.write(str)

    else: 
        latexContent.write(str)
    

##
# MAIN: Creates an html file containing a formatted htm tutorial
# layout. The LaTeX generator takes the generated html code and
# outputs a formatted LateX copy.
##

# Global Variables
tp_url = "https://www.tutorialspoint.com/"

tut_ext = input("Which Tutorial: ")
tut_ext = tut_ext.lower()
if tut_ext.find(' ') != -1:
        tut_ext = underscoreSep(tut_ext)
        print(tut_ext)

htmlContent = open(tut_ext + ".html", "a+")

latexContent = open(tut_ext + ".tex", "a+")

### Get tutorial and tutorial extensions list ###
getList(tp_url)


### html generator ###
htmlContent.write("<!DOCTYPE html>")
htmlContent.write("<html>")
htmlContent.write("<body>")

with open(tut_ext + ".tut.list2", "r") as f:
   for ext in f:
      getTutorial(ext)

htmlContent.write("</body>")
htmlContent.write("</html>")

htmlContent.close()
os.system("rm " + tut_ext + ".tut*")


### LaTeX generator ###

latexContent.write(r"\documentclass[12pt]{article}")
latexContent.write("\n")
latexContent.write(r"\usepackage{amsmath}")
latexContent.write("\n")
latexContent.write(r"\usepackage{graphicx}")
latexContent.write("\n")
latexContent.write(r"\usepackage{hyperref}")
latexContent.write("\n")
latexContent.write(r"\usepackage[latin1]{inputenc}")
latexContent.write("\n")
latexContent.write(r"\usepackage{fancyhdr}")
latexContent.write("\n")
latexContent.write(r"\pagestyle{fancy}")
latexContent.write("\n")
latexContent.write(r"\rfoot{\thepage}")
latexContent.write("\n")
latexContent.write(r"\date{\today}")
latexContent.write("\n")
latexContent.write(r"\begin{document}")

with open(tut_ext + ".html", "r") as f:
   for ext in f:
      latex(ext)

latexContent.write(r"\end{document}")

latexContent.close()
os.system("rm *~")
os.system("rm *.tex")
