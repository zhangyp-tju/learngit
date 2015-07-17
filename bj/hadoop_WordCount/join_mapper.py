#!/usr/bin/env python

import sys

def split_add_tag(line):
    words = line.split()
    flag = 1
    for word in words:
        if flag:
            flag=0
            continue
        print '%s\t%s' % (word, "1\t" + line)

def just_add_tag(line):
    words = line.split(' ',1)
    if len(words) != 2:return
    new_line = "2\t" + words[1]
    print '%s\t%s' % (words[0],new_line)

flag = 5

if __name__ == "__main__":
    '''join two files'''
    for line in sys.stdin:
        line = line.strip()
        if not line:continue
        if(len(line.split()) > 5):
            split_add_tag(line)
        else:
            just_add_tag(line)
