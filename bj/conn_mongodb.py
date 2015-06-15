#!/usr/bin/python
#-*-encoding:utf-8-*-
# mongodb install : ubuntu12.04 --- 32bit --- 
'''
(1)apt-get install mongodb-server
(2)mongodb-linux-x86_64-ubuntu1204-3.0.3.tgz unzip -->bin$ mongod -port 27017 --dbpath ../data --logpath ../log/mongodb.log
(3)bin$ mongo localhost:27017  ---> connecting to test and you can operator mongo
(4) pip install pymongo or apt-get install pymongo is so easy
(5)someples....
'''
from pymongo import MongoClient
import random

#conn=pymongo.Connection(host="127.0.0.1",port=27017)#has no atrri Connection

#db = conn.tage #连接库
#db.authenticate("tage","123")
#用户认证

conn = MongoClient('127.0.0.1',27017)
db = conn.test

#coll = MongoClient("students")


#db.students.drop()

#删除集合students
coll = db.students
coll.insert({'id':1,'name':'kaka','sex':'male'}) # coll.save() is wrong

#插入一个数据

for id in range(2,10):
	name = random.choice(['steve','koby','owen','tody','rony'])
	sex = random.choice(['male','female'])
	coll.insert({'id':id,'name':name,'sex':sex})
#通过循环插入一组数据

# update
print "***%s" %coll.find_one()# get the first line
coll.update({'id':2},{'$set':{'name':'zzzzz','sex':'man'}})# can't add  ag
# delete one line using remove..
coll.remove({'id':3}) # must be string key
coll.update({},{'$set':{'age':1,'birth':'2015.06.15'}},upsert=True,multi=True)
print "size is %s" % db.students.find().count()
content = db.students.find()

#打印所有数据

for i in content:
	print i
print "ending..."
