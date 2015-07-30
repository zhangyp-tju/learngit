#!/bin/bash
#-*-encoding:utf-8-*-

# Author : zyp
# Written : Jun 24, 2015
# Modified : 
# Purpose : python call for shell and python call for c
host=`hostname -i` # get local IP
set -x 
# sdb open debugger the shell script
workdir=`pwd`
printf "BEGIN...in ${host} and ${workdir}\n"
name='xqz'
printf "hello, python call shell file ${name}\n" 
if test ${name} = "xqz"
then
    printf "test insdead of [ ] $0 variable\n"
fi
set -m
# monitor
set -o
if test $# -gt 0 -a $# -ne 1;then
    # $# the params numbers and $* the list of params and $1,$2....
    # $0 is the shell script itself not in $*
    printf "$*,,,$@\n"
fi
set +x
# close the debugge model
printf "END...\n"
# end
