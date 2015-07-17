#!/usr/bin/python2.6 

import sys

current_key = None
current_value = None
key = None

def conbine_value(line):
    global current_key,current_value,key
    try:
        key,value = line.split('\t')
    except:
        return
    if current_key == key:
        current_value = current_value + " " + value
    else:
        if current_key:
            print "%s\t%s" % (current_key.split()[0],current_value)
        current_key = key
        current_value = value



if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        if not line:continue

        conbine_value(line)
    if current_key == key:
        print "%s\t%s" % (current_key.split()[0],current_value)
