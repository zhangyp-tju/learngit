#!/sur/bin/python
#-*- encoding:utf-8 -*-

# Author: zyp
# Writtern: Apir 24,2015
# Purpose: just for json

def file_do(filepath):
	# with expression as target
	with open(filepath,'rt') as fr:
		for line in fr:
			print line
			# ...more code

def file_old(filepath):
	# the old and traditional access
	fr = open(filepath,'rt')
	try:
		for line in fr:
			print line
			# ...more code
	finally:
		fr.close()

# little using
class closing(object):
	#
	def __init__(self,thing):
		self.thing = thing
	def __enter__(self):
		return self.thing
	def __exit__(self,*exc_info):
		self.thing.close()

class ClosingDemo(object):
	def __init__(self):
		self.acquire()
	def acquire(self):
		print "Acquire resources."
	def free(self):
		print "Clean up any resources acquired."
	def close(self):
		self.free()

# more use

from contextlib import contextmanager

@contextmanager
def demo():
	print "[A2 locate resources]"
	print "Code before yield-statement executes in __enter__"
	yield "*** contextmanager demo ***"
	print "Code after yield^"
	print "[Free resources]"

print "***** test for MySQLdb: *****"


import MySQLdb
# establish connection with mysql
conn = MySQLdb.connect(host='localhost',user='root',passwd='root')
# get the cursor of operator
cur = conn.cursor()
# execute sql and create database name/ drop database name
cur.execute("""create database if not exists python""")
# select database use database
conn.select_db('python')
# execute and create table
cur.execute("""create table test(id int,ifo varchar(100))""")

value = [1,"inserted?"]
# insert one record
cur.execute("insert into test values(%s,%s)",value)

values=[]
for i in range(20):
	values.append((i,'Hello mysqldb,I am record' + str(i)))
# insert multi records
cur.executemany("""insert into test values(%s,%s)""",values)
# close cursor
cur.close()

print "create successfully!"

#conn = MySQLdb.connect(host = 'localhost', port = '3306', user = 'root', passwd = 'root', db = 'test')
#cur = conn.cursor()


#cur.close()
# commit and close the connection
conn.commit()
conn.close()
if(__name__ == "__main__"):
	print "test for important with:"
	file_do("./test.txt")
	
	print "the old access to compare with the above method \'with\'"
	file_old('./test.txt')

	print "test for closing method:"
	with closing(ClosingDemo()):
		print "Using resources"

	print "test for contextmanager from contextlib:"
	with demo() as value:
		print "Assigned Value: %s" % value
