#!/sur/bin/python
#-*- encoding:utf-8 -*-

# Author: zyp
# Writtern: Apir 22,2015
# Purpose: just for json

import json

print "just for json dumps and dump:"
dic = dict(name="tju", birth=1895, addr="tju.edu.cn")
str = json.dumps(dic)
print str
json_file = "./json.txt"
f = open(json_file,'w')#a append
json.dump(dic,f)
f.close()

print "just for json loads and load:"
json_str = str
print json.loads(json_str)
#json_rfile = "./json_source.dat"
f = open(json_file,'r')
s = json.load(f)
print s
f.close()

print "*** json important serialization by your model: ***"
class School(object):
   def __init__(self, name, birth, addr):
      self.name = name
      self.birth = birth
      self.addr = addr
   def prints(self):
      print "name-->%s" % self.name
      print "birth-->%s" % self.birth
      print "addr-->%s" % self.addr


def school2dict(std):
   return {
      'name':std.name,
      'birth':std.birth,
      'addr':std.addr
   }

school = School('tju',1895,'tju.edu.cn')
#print (json.dumps(school, default=school2dict))#or
#or more usefully
str = (json.dumps(school, default=lambda obj:obj.__dict__))
fw = open("./test.txt",'w')
json.dump(school,fw,default=school2dict)
print str
fw.close()

def dict2school(d):
   return School(d['name'], d['birth'], d['addr'])


json_str = str
s = (json.loads(json_str, object_hook=dict2school))
s.prints()
fr = open('./test.txt','r')
sr = json.load(fr,object_hook=dict2school)
sr.prints()
fr.close()

print "just for readlines by size:"

fw = open('./test2.txt','wt')
fr = open('./generator_genelist.py','rt')
sizehint = 8096 # 8K
position = 0
lines = fr.readlines(sizehint)
fw.writelines(lines)
print "lines %s" %lines
# then we can splits the lines and operator what we want
while not (fr.tell() - position > 0):
	position = fr.tell() # Python tell() return the point of file r or w
	lines = fr.readlines(sizehint)
	print "lines %s" %lines
	fw.write(lines)

fr.close()
fw.close()
