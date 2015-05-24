#!/usr/bin/python
#-*- coding:utf-8 -*-

# Author: zyp
# Writtern: May 11,2015
# Purpose: just for test Map and Reduce function

print "***just for map ***"
l = map(lambda x: x%3, range(6))
print l

ll = [i for i in range(6) if i%2 == 0]
print ll
l = map(lambda x,y,z: (x-y+z, x+y+z, x+y-z),range(3),ll,range(4,7))
print l

print "***just for reduce ***"
n = 5
print reduce(lambda x,y: x*y, range(1, n+1))

m = 2
n = 5
print reduce(lambda x,y: x*y, range(1,n+1),m)

