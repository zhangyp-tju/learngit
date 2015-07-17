#!/usr/bin/python2.6 

import sys

def just_split(line):
    try:
        key,value = line.split('\t')
    except:
        return
    print '%s\t%s' % (key,value)
    


if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        if not line:continue
        just_split(line)
