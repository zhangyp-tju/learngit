#!/usr/bin/python
#-*- coding:utf-8 -*-

# Author: zyp
# Writtern: May 30,2015
# Purpose: just for test Map and Reduce function -- word count function

from operator import itemgetter
from itertools import groupby
import sys

def read_mapper_output(file, regex = '\t'):
	for line in file:
		yield line.rstrip().split(regex, 1)

def main(regex = '\t'):
	data = read_mapper_output(sys.stdin,regex = regex)
	for current_word, group in groupby(data, itemgetter(0)):
		try:
			total_count = sum(int(count) for current_word, count in group)
			print "%s%s%d" % (current_word, regex, total_count)
		except valueError:
			pass

if __name__ == "__main__":
	main()

