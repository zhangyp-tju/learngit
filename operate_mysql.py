#!/usr/bin/python
#-*- encoding:utf-8 -*-

# Author: zyp
# Writtern: Apir 24,2015
# Purpose: just for json
# common command --- the same to cmd consel ---- mysql -u root -p --
# mysql -- show databases; -- create database name -- use dbname --
# drop database name -- create table name (id int, name varchar(100)) --
# select * from tbname (where) / delete from tbname where -- desc tbname
# insert into tbname values(1,'zyp') / update tbname set id=99 where id=9

import MySQLdb

conn = MySQLdb.connect(host='localhost', user='root', passwd='root', db='python')
cur = conn.cursor()
sql = 'select * from test'
# select is not needed, I think; but the insert and delete, update need to 
# commit and rollback operations
try:
	count = cur.execute(sql)
	print "The total number of records is %s record(s)." %count
	conn.commit()
except:
	conn.rollback()

print "fetchone() get one record:"
res = cur.fetchone()
print 'ID:%s info:%s' % res

print "fetchmany() get many records:"
res = cur.fetchmany(5)
for ele in res:
	print 'ID:%s info:%s' % ele

# reset the cursor
cur.scroll(0,mode='absolute')
print "fetchall() get all records:"
res = cur.fetchall()
for ele in res:
	print 'ID:%s info:%s' % ele

# reset the cursor
cur.scroll(0,mode='absolute')
print "select where :"
sql = "SELECT * FROM test WHERE id > %d and \
       ifo = '%s'" % (5,'Hello mysqldb,I am record6')
try:
	cur.execute(sql)
	res = cur.fetchall()
	for ele in res:
		print "ID: %s, info: %s" %ele 
except:
	print "Error: unable to fetch data"

cur.close()
conn.commit()

print "operate activity:"
cur = conn.cursor()
sql = "UPDATE test SET ifo = '%s'\
       WHERE id < %d" %('changed already',4)
try:
	cur.execute(sql)
	conn.commit()
except:
	# error and rollback
	conn.rollback()

print "fetchall after update:"
sql = "select * from test"
try:
	cur.execute(sql)
	res = cur.fetchall()
	for ele in res:
		print "ID: %d, info: %s" %ele
except:
	print "Error: can\'t fetch data"
conn.close()
