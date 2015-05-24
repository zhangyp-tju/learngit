#!/usr/bin/python
#-*- encoding:utf-8 -*-

# Author: zyp
# Writtern: May 12, 2015
# Purpose: just for test

print "generate list:"
print [x*x for x in range(1,11) if x%2 == 0]

print "Generator: [] --> ()"
gene = (x*x for x in range(1,11) if x%2 ==0)
for n in gene:
   print n
print gene

# fib --> generator
print "fib --> generator for yield:"
def fib(max):
   n, a, b = 0, 0, 1
   while n < max:
      print b
      a, b = b, a+b
      n = n+1
n = input("Please input your number:\n")
fib(n)

def fib(max):
   n, a, b = 0, 0, 1
   while n < max:
      yield b
      a, b = b, a+b
      n = n+1
n = input("Please input your number:\n")
for n in fib(n):
   print n

print "just for filter:"
def is_odd(n):
   return n%2 == 1
print filter(is_odd, range(1,11))

print "just for map + reduce:"
def str2int(s):
   dict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
   def fn(x, y):
      return x*10 + y
   def char2num(s):
      print dict[s]
      return dict[s]
   return reduce(fn,map(char2num, s))

print str2int('1895')


