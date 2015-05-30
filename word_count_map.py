#!/usr/bin/python
#-*- coding:utf-8 -*-

# Author: zyp
# Writtern: May 30,2015
# Purpose: just for test Map and Reduce function -- word count function

import sys

# this map just cin from cat and cout (word,1)
def word_map():
	for line in sys.stdin:
		line = line.strip()
		words = line.split()
		for word in words:
			print "%s\t%s" % (word,1)
# call the function
word_map()
# readme please and excecute this command:
# chmod +x word_count_reduce.py word_count_map.py
# cat datafile | ./word_count_map.py | sort | ./word_count_reduce
# print results in cmd.


