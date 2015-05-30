#!/usr/bin/python
#-*- coding:utf-8 -*-

# Author: zyp
# Writtern: May 30,2015
# Purpose: just for test Map and Reduce function -- word count function

import sys

def read_input(file):
	for line in file:# read line by line is very low, not quick than readlines()
		yield line.split()# str.split(str=" ",num=string.count(str))

def main(regex='\t'):
	data = read_input(sys.stdin)
	#print "data:",data
	for words in data:
		#print "words:", words
		for word in words:
			print "%s%s%d" % (word, regex, 1)
if __name__ == "__main__":
	main()
