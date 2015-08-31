#!/usr/bin/python2.6
#coding=utf-8

from datetime import datetime
import time
import sys
import os


def statistic_by_month(file_in,outfile):
    #outfile = "%s%s" % (str(file_in) , ".csv")
    print outfile
    fw = open(outfile,'w')
    regex = '\t'
    with open(file_in,'r') as fr:
        for line in fr:
            cnt_cishu = 0
            line = line.strip()
            if not line: continue
            #days_list = []
            eles = line.split(regex)
            try:
                days = len(eles) - 2 # 发文的总天数，发文频率
                open_id = eles[0] # 已经带有5级标示
                mon_cnt = eles[1] # 一个月总发文文章总数
                for i in range(2,len(eles)):
                    cishu = eles[i].split("#",1)[1]
                    cnt_cishu += len(cishu.split('_')) # 发文的次数，一天可以发多次
            except:
                print line
            avg_cishu = "%.1f" % (float(mon_cnt)/cnt_cishu)
            fw.write(open_id +","+ mon_cnt +","+ str(days) +","+ str(avg_cishu) +"\n")
            #break
    fw.close()
# 这个非常类似statistic_fawen_byopenid_2.py 只是统计的指标不同而已
def main():
    current_path = os.getcwd()
    print "参数0：%s" % (sys.argv[0])
    if len(sys.argv) < 3:
        print >> sys.stderr,"ERROR CMD(main_statistic_openid_timestamp)...Usage:tatistic_fawen_byopenid.py [FOLDER_SRC] [FILE_OUT]"
        exit(1)
    file_in = os.path.join(current_path,sys.argv[1])
    file_out = os.path.join(current_path,sys.argv[2])
    if not os.path.isfile(file_in):
        print >> sys.stderr, "ERROR: %s" % (file_in)
        exit(1)
    print file_in
    statistic_by_month(file_in,file_out)


if __name__ == "__main__":
    main()


