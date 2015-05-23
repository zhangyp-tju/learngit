# coding=utf-8
#!/usr/bin/python

print " *********just for test file i/o******";	
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

print " *********just for test file i/o compare for above method ******";	
try:
	fileR = open('splits.txt','r');
	f_lines = fileR.readlines();
	for line in f_lines:
		eles = line.split(',');
		#print eles.pop(); #默认删除最后一个元素
		#print len(eles); # list的元素个数
		for ele in eles:
			if(ele[-1] == '\n'):
				ele = ele[:-1]; #截取从开头到 倒数第一个字符（倒数第一个去掉）
			print ele;
except IOError:
	print "Error:can\'t find this file";
fileR.close();

print " *********just for operate list******";

list = ['physics', 'chemistry', 1997, 2000];
# append 追加元素 自添加多少倍
list = list + ['zyp','xqz'];
list = list*3;
print "list: ", list;
# 通过下标截取，删除
print "list[1:4] [eles): ",list[1:4];
print "len(list[1:4]: ", len(list[1:4]);
print "list[-2]:", list[-2];
print "list[:4]:", list[:4];
print "list[2:]:",list[2:];
del list[8:-1];
print "after del list[8:-1]: ", list

print "list.pop(): ",list.pop();
print "list.count('zyp'): ", list.count('zyp');

print " *********just for operate string******";
#续行符
line = "I am zyp, from HKU,\
my name is Minzhang.\
Welcome my zoon!\a";
print line;
#自连接 多少倍
line = line*3;
# find() count() len() index() 下标取值
print "line.count('zyp',2,len(line)-1):  ",line.count('zyp',2,len(line)-1);
print "substr: ", line[line.find('zyp',2,15):line.find('zyp')+len('zyp')];
# replace() splite()分隔
print "line.replace('zyp','cxt'):", line.replace('zyp','cxt');
words = line.split(',');
for word in words:
	print word;

print "********line or lines****"
lines = '''
I am zyp, from HKU,
my name is Minzhang.
Welcome my zoon!
''';
print lines;
errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
''';
print errHTML;

print "********dict_hash****";

dict_hash = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'};
print "dict_hash['Beth']: ", dict_hash['Beth'];
#insert or add
dict_hash['name'] = 'zyp';
print "dict_hash['name']:",dict_hash['name'];
#change the value by key
dict_hash['name'] = 'cxt';
#get the all keys and traversal
keys = dict_hash.keys();
for key in keys:
	print key,"-->",dict_hash.get(key);
# change from hash to vector
items = dict_hash.items();
for item in items:
	print item;
print "dict_hash.has_key('cxt'):", dict_hash.has_key('cxt'),"; dict_hash.has_key('name')", dict_hash.has_key('name');

print "********function test****";
#匿名函数的声明和调用
sum = lambda arg1,arg2:arg1 + arg2;
print "Value of total sum(10,20)", sum(10,20);
print "Value of total sum(20,20)", sum(20,20);
#可写函数说明 和 不定长参数
def printinfo(arg1,*vartuple):
	"打印任何传入的参数"
	print "output:";
	print arg1;
	for var in vartuple:
		print var;
	return;
printinfo(10);
printinfo(70,60,50);


print "***********try except********";
# 自定义异常 使用raise语句自己触发异常
class NetworkError(RuntimeError):
	def __init__(self,arg):
		self.args = arg;
try:
	raise NetworkError("Bad hostname");
except NetworkError,e:
	print e.args;
	print str(e);
except "Invalid levele!":
	print "Invalid levele!";
finally:# 对出try时总会执行
	print "can\'t find ";
prompt = "***********Module 模块就是.py文件********";
print prompt.decode('gbk').encode('utf8');#cao 这都不行，中文还是乱码，真是无语了
# 若去掉global就不对啦
Money = 2000;
def AddMoney():
	"想改正代码就取消以下注释"
	global Money;
	Money = Money + 1;
	print Money;
	return;
print "before recall AddMoney:", Money;
AddMoney();
print "after recall AddMoney:", Money;





