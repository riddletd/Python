#!/usr/bin/env python3

######################################################################
#
# I simple web scraper used for learning.
#
# Author: Trevor Riddle
# Creation Date: May 31, 2017
# Update: -
#
######################################################################

import os, sys, requests

papa_johns_url = "https://www.papajohns.com/order/menu/pizza/pepperoni1"
post = requests.post(papa_johns_url, data={'sourceURL':'Site_trigger_AddToCart.js'})
print(post.text)
