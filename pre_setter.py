#!/usr/bin/python
#-*- encoding:utf-8 -*-

# Author: zyp
# Writtern: Apir 24,2015
# Purpose: just for using @property insdead of setter() and getter()
#

class Student(object):
	
	def __init__(self, name, birth):
		self._name = name
		self._birth = birth
	
	# both read and write(birth)
	@property
	def birth(self):
		return self._birth
	
	@birth.setter
	def birth(self, value):
		self._birth = value

	#read-only(age)
	@property
	def age(self):
		return 2014 - self._birth

	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, value):
		self._name = value

	def shuchu(self):
		print "name: %s\nbirth: %d\nage: %d" \
		%(self.name, self.birth, self.age)

if(__name__ == "__main__"):
	print "just for @property:"
	st = Student('zyp',2000)
	st.shuchu()
	st.birth = 1989
	st.name = 'xqz'
	st.shuchu()
	#print "",st.birth() # Error:TypeError: 'int' object is not callable
	# because you have set the function birth as property
else:
	print "not in this model"
