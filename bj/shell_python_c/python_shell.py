#!/usr/bin/python2.6
#-*-encoding:utf-8-*-

'''
# Author : zyp
# Written : Jun 24, 2015
# Modified : 
# Purpose : python call for shell and python call for c
'''

import commands

def cmd_st_out():
    
    (status, output) = commands.getstatusoutput("ls ./")
    print "status: %s\nls ./: %s" %(status, output)

def cmd_st_out_file():
    #file_sh = 'sh ./call.sh'# also can execute
    file_sh = './call.sh'# need the right path !/bin/bash and need executed rithts
    print commands.getstatusoutput(file_sh)
    (status, output) = commands.getstatusoutput(file_sh)
    print status, output

import subprocess

def subprocess_popen():
    file_sh = "./call2.sh"
    subprocess.Popen(file_sh,shell=True)
    print "ending..."

# call c
import os
from ctypes import*

def cdll_c():
    #libtest = cdll.LoadLibrary(os.getcwd()+'/libtest.so')
    call2 = cdll.LoadLibrary(os.getcwd()+'/call2.so')
    print call2.multiply(5,8)
    print "python :%s" %call2.output("all")
    call2.main()

def cdll_cc():
    
    call = cdll.LoadLibrary(os.getcwd()+'/call.so')
    #print call.multi(5,5)
    call.main()

if (__name__ == "__main__"):
    cmd_st_out()
    cmd_st_out_file()
    subprocess_popen()
    print "*******call for shell above*** call for c following*********"
    cdll_c()
    cdll_cc()




