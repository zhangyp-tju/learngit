# encoding: utf-8
#!/usr/bin/python
import re

class Parent:
	parentAttr = 100;
	# 重载
	def __init__(self):
		print "调用父类构造函数 Parent construct".decode("utf-8").encode("gbk");
	#成员函数
	def parentMethod(self):
		print "调用父类成员函数:Parent method";
	def setAttr(self,attr):
		Parent.parentAttr = attr;
	def getAttr(sef):
		print "父类属性：ParentAttr:", Parent.parentAttr;
	def __del__(self):
		print "parent descontruct";
	
	
class Child(Parent): # 定义子类
	def __init__(self):
		print "调用子类构造方法 child construct"

	def childMethod(self):
		print '调用子类方法 child method'
	def __del__(self):
		print "child destructor";

c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法
c.getAttr()  


lines = "zyp,0001,nan\r\nxqz,0002,nan\r\nwzx,0003,nv";
line = "Cats are smarter than dogs";
matchObj = re.match( r'(.*),', lines, re.M|re.I)

if matchObj:
	print "ddd", matchObj.group();
else:
	print "no match!!";
lists = lines.split(',\\r\\n');
print "lists:",lists;

for li in lists:
	print li;
	#print li,"\n";

print " *********just for test******";	
try:
	fileR = open('splits.txt','r');
	done = 0;
	while not done:
		f_str = fileR.readline();
		if (f_str != ''):
			eles = f_str.split(',');
			#print "eles:",eles;
			for ele in eles:
				print ele;
		else:
			done = 1;
except IOError:
	print "Error:can\'t find this file";
fileR.close();

print " *********just for test******";	
try:
	fileR = open('splits.txt','r');
	f_lines = fileR.readlines();
	for line in f_lines:
		eles = line.split(',');
		for ele in eles:
			print ele;
except IOError:
	print "Error:can\'t find this file";
fileR.close();
