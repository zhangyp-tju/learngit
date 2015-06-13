#!/usr/bin/python2.6
#-*-encoding:utf-8-*-
'''
auther: zyp
data: june 8,2015
'''
import sys
#import tab # using in this mode tab.function()
from tab import * # using in another mode function(),but this is forbidden ½ûÖ¹

def main(filepath):
	old_sysout = None
	logfile = None
	try:
		logfile = open(filepath,'a')
		old_sysout = sys.stdout
		sys.stdout = logfile
		print "this is just for test logfile, and the file path is : %s" %filepath
	finally:
		if logfile:
			logfile.close()
		if old_sysout:
			sys.stdout = old_sysout
	print "Hello world in screen!"

def this_log():
	filepath = os.path.join(os.getcwd(),'log_zyp')
	this_file = os.path.join(os.getcwd(),__file__)
	#this_file = os.path.join(os.getcwd(),os.path.realpath(sys.argv[0]))
	print this_file
	logging.basicConfig(filename = filepath, level = logging.INFO,\
	format = "%(asctime)s - %(levelname)s >>> %(message)s" )
	log = logging.getLogger("root.txt")
	log.setLevel(logging.WARN)
	log.debug(this_file + " -- debug....")
	log.warn(this_file + " -- warn....")
	log.error(this_file + " -- error....")
	logging.debug("This is debug message>>>")
	logging.info("This is info message>>>")
	logging.warn("This is warning message>>>")
	logging.error("This is error message>>>")
# more useful log for python models
import logging
import logging.config
# just for conf file
def log_conf():
	logging.config.fileConfig('logging.conf')	
	this_file = os.path.join(os.getcwd(),__file__)
	root_log = logging.getLogger('root')
	root_log.debug(this_file + " -- root_log debug...")
	root_log.warn(this_file + "-- root_log warn...")

	my_log = logging.getLogger('mymain')
	my_log.info(this_file + " -- my_log info...")
	my_log.error(this_file + " -- my_log error....")


if (__name__ == "__main__"):
	filepath = './log_zyp'
	main(filepath) 
	#tab.test_log()
	test_log()
	this_log()
	# more useful
	log_conf()
