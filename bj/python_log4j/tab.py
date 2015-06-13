#!/usr/bin/evn python2.6
#-*-encoding:utf-8-*-

'''
Author: zyp
Written: June 9, 2015
Modified: June 9, 2015
Purpose: just for set ts=4--> set expandtab-->%rebab!
'''
import sys
import logging
import os

def main():
	flag = 0
	for filepath in sys.argv:
		if not flag:
			print "The %d time, and the file path is %s..." % (flag,filepath)
			flag = 1;
			continue
		elif flag == 1:
			print "The %d time, and the file path is %s..." % (flag,filepath)
			print "Do someting in the this seg..."
			flag = 4
		else:
			print "The %d time, and the file path is %s..." % (flag,filepath)
			print "Do someting..."
		test_log()

# just for test log
def test_log():
	filepath = os.path.join(os.getcwd(),'log_zyp')
	this_file = os.path.join(os.getcwd(),__file__)
	#this_file = os.path.join(os.getcwd(),os.path.realpath(sys.argv[0]))
	print "the log file path is %s; and the src file (this file itself) is %s" %(filepath,this_file)
	#logging.basicConfig(filename = filepath, level = logging.DEBUG)
	#logging.basicConfig(filename = filepath,level = logging.WARN)
	logging.basicConfig(filename = filepath, level = logging.INFO,\
	filemode = 'a',format = "%(asctime)s - %(levelname)s >>> %(message)s" )
	log = logging.getLogger("root.txt")
	log.setLevel(logging.WARN)
	log.debug(this_file + " -- debug....")
	log.warn(this_file + " -- warn....")
	log.error(this_file + " -- error....")
	logging.debug("This is debug message>>>")
	logging.info("This is info message>>>")
	logging.warn("This is warning message>>>")
	logging.error("This is error message>>>")




if (__name__ == "__main__"):
	main()
