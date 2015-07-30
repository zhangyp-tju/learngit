#!/usr/bin/python
#coding:gbk

import sys
import os
import pdb

def setbit(index): # 从第零位开始的
    global dat
    dat = dat | (1<<(index))

def getbit(index):
    global dat
    #return (dat & (1<<index))#?1:0
    return 1 if (dat & (1<<index)) else 0
def clearbit(index):
    global dat
    dat = dat & (~(0x01)<<(index))

def setbit_new(index):
    global arr
    tmp = ((arr[index/8]) | (1<<(7-index%8)))
    arr[index/8] = tmp

#arr = [0] * 480000000
#arr = [0] * 48000000000
#MemoryError#
dat = 0
#MAX = 384000000
MAX = 384000

def strHash(ustring):
    h = 0
    for chr in ustring:
        num_chr = ord(chr)
        h = (31*h + num_chr) % MAX
    #print h
    return h
def hfHash(ustring): # xiao guo buhao
    h = 0
    cnt = 1
    for chr in ustring:
        num_chr = ord(chr)
        h = (num_chr*3*cnt) % MAX 
        cnt += 1
    #print h
    #return h % len(ustring)
    return h

def dekHash(ustring):
    h = len(ustring)
    for chr in ustring:
        num_chr = ord(chr)
        h = ((h<<5) ^ (h>>27) ^ (num_chr) )% MAX 
    #print h
    #return h % len(ustring)
    return h
def elfHash(ustring):
    h = 0
    x = 0
    for chr in ustring:
        num_chr = ord(chr)
        h = (h<<4) + num_chr
        x = h & 0xf0000000
        if not x:
            h = h ^ (x >> 24)
        h = (h & (~x)) % MAX
    #print h
    #return h % len(ustring)
    return h
def sdbmHash(ustring):
    h = 0
    for chr in ustring:
        num_chr = ord(chr)
        h = ((h<<6) + (h<<16) + (num_chr) - h )% MAX 
    #print h
    #return h % len(ustring)
    return h
def djbHash(ustring):
    h = 5381
    for chr in ustring:
        num_chr = ord(chr)
        h = ((h<<5) + h + num_chr) % MAX
    #print h
    #return h % len(ustring)
    return h

def bpHash(ustring):
    h = 0
    for chr in ustring:
        num_chr = ord(chr)
        h = ((h<<7) ^ (num_chr) )% MAX 
    #print h
    #return h % len(ustring)
    return h
def fnvHash(ustring):
    h = 0
    fnv_prime = 0x811C9DC5
    for chr in ustring:
        num_chr = ord(chr)
        h = ((h*fnv_prime) ^  num_chr) % MAX
    #print h
    #return h % len(ustring)
    return h
def apHash(ustring):
    h = 0xAAAAAAAA
    cnt = 0
    for chr in ustring:
        num_chr = ord(chr)
        h = (h ^ ( (h <<  7) ^ num_chr * (h >> 3) if not (cnt&1) else ~((h << 11) + num_chr ^ (h >> 5))) )% MAX
    #print h
    #return h % len(ustring)
    return h
def hflpHash(ustring): # none using
    h = 5381
    for chr in ustring:
        num_chr = ord(chr)
        h = ((h<<5) + h + num_chr) % MAX
    #print h
    #return h % len(ustring)
    return h


def is_same(rstring):
    
    rstring = rstring.strip()
    if not rstring:return True
    try:
        line,value = rstring.split(',',1)
    except:
        pass
    hash = strHash(line)
    flag = 0
    if getbit(hash):
        #print "1存在str %s" %line
        flag += 1
    else:
        setbit(hash)

    hash = dekHash(line)
    if getbit(hash):
        #print "2存在dek %s" %line
        flag += 1
    else:
        setbit(hash)

    hash = elfHash(line)
    if getbit(hash):
        #print "3存在elf %s" %line
        flag += 1
    else:
        setbit(hash)

    hash = hfHash(line)
    if getbit(hash):
        #print "4存在hf %s" %line
        flag += 1
    else:
        setbit(hash)

    hash = sdbmHash(line)
    if getbit(hash):
        #print "5存在sdbm %s" %line
        flag += 1
    else:
        setbit(hash)

    hash = djbHash(line)
    if getbit(hash):
        #print "6存在djb %s" %line
        flag += 1
    else:
        setbit(hash)
    
    if flag < 6:
        return False
    elif flag == 6:
        return True
    

if __name__ == "__main__":
    
    print "脚本名：%s" % sys.argv[0]
    for i in range(1,len(sys.argv)):
        print "第%d个参数：%s" % (i,sys.argv[i])
    for line in sys.stdin:
        line = line.strip()
        if not line:continue
        hash = strHash(line)
        flag = 0
        if getbit(hash):
            #print "1存在str %s" %line
            flag += 1
        else:
            setbit(hash)

        hash = dekHash(line)
        if getbit(hash):
            #print "2存在dek %s" %line
            flag += 1
        else:
            setbit(hash)

        hash = elfHash(line)
        if getbit(hash):
            #print "3存在elf %s" %line
            flag += 1
        else:
            setbit(hash)

        hash = hfHash(line)
        if getbit(hash):
            #print "4存在hf %s" %line
            flag += 1
        else:
            setbit(hash)
 
        hash = sdbmHash(line)
        if getbit(hash):
            #print "5存在sdbm %s" %line
            flag += 1
        else:
            setbit(hash)

        hash = djbHash(line)
        if getbit(hash):
            #print "6存在djb %s" %line
            flag += 1
        else:
            setbit(hash)
        

        '''
        hash = bpHash(line)
        if getbit(hash):
            print "7存在bp %s" %line
        else:
            setbit(hash)

        hash = fnvHash(line)
        if getbit(hash):
            print "8存在bp %s" %line
        else:
            setbit(hash)

        hash = apHash(line)
        if getbit(hash):
            print "9存在ap %s" %line
        else:
            setbit(hash)
        '''
   
    '''
    setbit(8)
    print dat
    #print setbit(0,1000000) # 原来是输出耗时太多的，置位的话是瞬间完成的
    #setbit(0,100000000) # 原来是输出耗时太多的，置位的话是瞬间完成的
    print "test..."
    #print unichr(setbit(0,10000))
    #arr = [0] * 48
    #setbit_new(100000000)
    setbit(3)
    setbit(0)
    print dat
    '''
