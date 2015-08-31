#!/bin/sh 
#coding=utf-8
# one arg (file): url name openid


#printf "$1,$2"
# 1 openid 2 tmpfile (source file)
python2.6  getOriAccount.py $1 $2 1> $2_ori
