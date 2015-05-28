#!/sur/bin/python
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
count = cur.execute('select * from test')
print "The total number of records is %s record(s)." %count

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

cur.close()
conn.commit()
conn.close()
