#!/usr/bin/python
#-*-coding:gbk

import sys
import os
import pdb

'''
全角/半角转换
http://www.pythonclub.org/python-scripts/quanjiao-banjiao
'''
def strQ2B1(ustring):
    '''把字符串全角转半角'''
    rstring = ""
    ustring = ustring.decode("gbk","ignore")
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288:
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374):
            inside_code -= 65248
        rstring += unichr(inside_code)
    return rstring.encode("gbk","ignore")

def strB2Q(ustring):
    '''把字符串半角转全角'''
    rstring = ""
    ustring = ustring.decode("gbk","ignore")
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code<0x0020 or inside_code>0x7e: 
            rstring += uchar
        if inside_code==0x0020:
            inside_code=0x3000
        else:
            inside_code+=0xfee0
        rstring += unichr(inside_code)
    return rstring.encode("gbk","ignore")

