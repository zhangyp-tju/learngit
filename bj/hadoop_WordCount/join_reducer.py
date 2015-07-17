#!/usr/bin/python2.6 

import sys

current_key = None
current_value = None
key = None
def conbine_by_key(line):
    global current_key,current_value,key # attation thi for global
    key,flag,value = line.split('\t',2)
    try:
        flag = int(flag)
    except ValueError:
        return
    if current_key == key:
        if flag == 1: # come from file 1,meanwhile it mean the current_value = file 2's value
            current_value = value + "\t" + current_value
        else: # come from file 2
            current_value = current_value + "\t" + key + " " + value # key + value need in file 2 
    else:
        if current_key:
            #print '%s\t%s' % (current_key,current_value)
            print '%s' % (current_value)
        if flag == 1:
            current_key = key
            current_value = value
        else:
            current_key = key
            current_value = key + " " + value

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        if not line:cotinue

        conbine_by_key(line)
    # print the last one if exists
    if current_key == key:
        print '%s' % (current_value)
