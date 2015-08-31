#!/usr/bin/python2.6
#coding=utf-8

from datetime import datetime
import time
import sys
import os

open_id_5_dic = {}
# 五级账号
def load_open_id_5():
    filename = "./openid_level5_20150807"
    with open(filename,'r') as fw:
        for line in fw:
            line = line.strip()
            if not line: continue
            open_id_5_dic[line] = 1



def statistic_by_day(file_in,outfile):
    #outfile = "%s%s" % (str(file_in) , "_final")
    print outfile
    fw = open(outfile,'w')
    regex = '\t'
    with open(file_in,'r') as fr:
        for line in fr:
            line = line.strip()
            if not line: continue
            #days_list = []
            eles = line.split(regex)
            try:
                open_id = eles[0]
                mon_cnt = eles[1]
            except:
                print line
            eles_len = len(eles)
            days_dic = {} # 存放 key = day,value 是各个group的数量
            for i in range(2,eles_len): # cong 2 (第三列)开始
                time_list = eles[i].split('-') # 每一个group的timestamp
                time_str = datetime.fromtimestamp(int(time_list[0])).strftime("%Y%m%d %H:%M:%S") # 获取改组的时间戳
                #print type(time_str)
                day = time_str[4:8] # 开始的day 即 key
                if day not in days_dic:
                    days_dic[day] = []
                group_cnt = len(time_list) # 每一天的累积
                days_dic[day].append(str(group_cnt) )
                #print start
            # 排序 按照day
            days_list_sort = sorted(days_dic.items(),key=lambda d:d[0],reverse=True)
            if open_id in open_id_5_dic:
                fw.write("5--" + open_id + "\t" + mon_cnt + "\t")
            else:
                fw.write(open_id + "\t" + mon_cnt + "\t")
            for day,group_list in days_list_sort:
                day_cnt = 0
                for cnt in group_list:
                    day_cnt += int(cnt)
                fw.write(day + "_" + str(day_cnt) + "#"  + '_'.join(group_list) + "\t" )
            fw.write("\n")
            #break
    fw.close()

def main():
    current_path = os.getcwd()
    print "参数0：%s" % (sys.argv[0])
    if len(sys.argv) < 3:
        print >> sys.stderr,"ERROR CMD(main_statistic_openid_timestamp)...Usage:tatistic_fawen_byopenid.py [FOLDER_SRC] [FILE_OUT]"
        exit(1)
    file_in = os.path.join(current_path,sys.argv[1])
    file_out = os.path.join(current_path,sys.argv[2])

    load_open_id_5()
    if not os.path.isfile(file_in):
        print >> sys.stderr, "ERROR: %s" % (file_in)
        exit(1)
    print file_in
    statistic_by_day(file_in,file_out)


if __name__ == "__main__":
    main()






