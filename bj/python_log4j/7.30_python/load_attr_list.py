#!/usr/bin/python2.6 
#coding=gbk

import sys

def get_attr_list():
    ''''''
    file_path = './attr.data'
    attr_list = ['kong']
    regex = '//'
    with open(file_path) as fp:
        for line in fp:
            line = line.strip()
            if not line: continue
            try:
                words = line.split(regex,1)
            except:
                print >> sys.stderr, "ERROR words ...."
            #print words[1].strip()
            attr_list.append(words[1].strip())
        print "in function"
        print attr_list
        return attr_list
if __name__ == "__main__":
    attr_list = []
    regex = '//'
    for line in sys.stdin:
        line = line.strip()
        if not line: continue
        try:
            words = line.split(regex,1)
        except:
            print >> sys.stderr, "ERROR words ...."
        attr_list.append(words[1].strip())

    print attr_list
    get_attr_list()
