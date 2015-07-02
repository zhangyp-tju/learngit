#!/bin/bash
#-*-encoding:utf-8-*-

# Author : zyp
# Written : Jun 24, 2015
# Modified : 
# Purpose : python call for shell and python call for c

name='xqz'
num=3 #empty cap is forbidden...
if test "${name}" = "xqz" && test ${num} -gt 1
then
	printf "test for if test - then - fi in shell\n"
fi

if [ $num -eq 3 -a $num -lt 1 ] && [ "${name}" = "xqz" ];then
	printf "test for if -then- fi in shell\n"
elif [ $num -eq 3 ];then
	printf "the num is ${num}\n"
else
	printf "others...\n"

fi

