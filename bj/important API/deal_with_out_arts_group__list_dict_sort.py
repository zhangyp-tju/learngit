#!/usr/bin/python2.6 
#coding=utf-8

from datetime import datetime
import time
import sys
import os

open_id_5_dic = {}

def load_open_id_5():
    filename = "./openid_level5_20150807"
    with open(filename,'r') as fw:
        for line in fw:
            line = line.strip()
            if not line: continue
            open_id_5_dic[line] = 1



def statistic_by_day_old():
    outfile = "final_result"
    fw = open(outfile,'w')
    regex = '\t'
    for line in sys.stdin:
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
            time_str = datetime.fromtimestamp(int(time_list[0])).strftime("%Y-%m-%d %H:%M:%S") # 获取改组的时间戳
            #print type(time_str)
            day = time_str[0:10] # 开始的day 即 key 
            time_time = time_str[11:] # 时刻
            if day not in days_dic:
                days_dic[day] = []
            group_cnt = len(time_list) # 每一天的累积
            days_dic[day].append(time_time + "-" + str(group_cnt) )
            #print start
        # 排序 按照day
        days_list_sort = sorted(days_dic.items(),key=lambda d:d[0])
        fw.write(open_id + "\t" + mon_cnt + "\t")
        for day,group_list in days_list_sort:
            day_cnt = 0
            for group in group_list:
                cnt = group.split('-')[1]
                day_cnt += int(cnt)
            fw.write(day + "@" + str(day_cnt) + "##"  + '_'.join(group_list) + "\t" )
        fw.write("\n")
        break
    fw.close()
# 重点 *** dict sort  list 截取 *******
# 不能够 int + str 的，得手动装换类型；sum(list) 必须是int;而join必须是str
def statistic_by_day():
    outfile = "final_result"
    fw = open(outfile,'w')
    regex = '\t'
    for line in sys.stdin:
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



if __name__ == "__main__":
    #cmd  cat out_arts_group | python2.6 deal_with_out_arts_group.py
    load_open_id_5()
    statistic_by_day()







