#!/usr/bin/env python
#coding=utf-8

import sys
import time
from datetime import datetime

openid_art = {}  # for load_openid()

def write_result(file_out):
    with open(file_out,'w') as fpw:
       for key, value in openid_art.items():
           fpw.write(key +"\t"+ str(value[0]) +"\t"+ str(value[1]) +"\t"+ str(value[2]) +"\n")

def statistic_ori_account(file_in):
    with open(file_in) as fpr:
        cnt = 0
        for line in fpr:
            line = line.strip()
            if not line: continue
            cols = line.split('\t')
            if len(cols) < 8:
                #print "******",len(cols)
                print "ERROR>>>",line
                cnt+=1
                continue
            try:
                openid_u_name = cols[-4]
                id_name = openid_u_name.split("##")
                #u_name = id_name[0]
                openid = id_name[1]
                fl = cols[-1]
                #print >> sys.stderr, "type", type(fl)
            except:
                #print >> sys.stderr,"ERROR ****",line
                cnt+=1
                #print "***",id_name[1],fl
                exit(1)
            openid_art[openid] = openid_art.get(openid,[0,0,0])
            if fl == "1":
                openid_art[openid][1] += 1 # 原创数目
            elif fl == "2":
                openid_art[openid][2] += 1 # 转载数
            openid_art[openid][0] += 1 # 文章总数

        print "ERROR: NUM-- %d" % (cnt)

def main():
    print "0:%s" % (sys.argv[0])
    if len(sys.argv) < 3:
        print >> sys.stderr,"ERROR CMD(main_statistic_openid_timestamp)...Usage:tatistic_fawen_byopenid.py [FOLDER_SRC] [FILE_OUT]"
        exit(1)
    print sys.argv[1],sys.argv[2]
    statistic_ori_account(sys.argv[1])
    write_result(sys.argv[2])


if __name__ == '__main__':
    main()
