#!/usr/bin/python
#-*-encoding:utf-8-*-

import sys
import pymongo
import time
from datetime import datetime

account_openid_rfb = {} # the main dicts


# read mongodb one by one and statistic
def statistic_ydb(file_in):
    #print "BEGIN STATISTIC(starting in mongodb)...%s" %time.strftime("%Y-%m-%d %H:%M:%S")
    with open(file_in) as fpr:
        for line in fpr:
            line = line.strip()
            if not line: continue
            cols = line.split("\t")
            if len(cols) < 4:
                continue
            account_openid = cols[0]
            #page_time = cols[1]
            read_num = int(cols[2])
            yuedu_fensi_bi = float(cols[3])
            #page_time_str = datetime.fromtimestamp(int(page_time)).strftime("%Y%m%d %H:%M:%S")
            if yuedu_fensi_bi == 0.0:
                continue
            # 合法数据总该执行的，第一个if判断是否合法的
            if account_openid not in account_openid_rfb:
                read_yfb = [0,0.0]
                read_yfb[0] = read_num
                read_yfb[1] = yuedu_fensi_bi
                account_openid_rfb[account_openid] = read_yfb
            else: # 把最小的read_num作为求粉丝数的人数
                if read_num < account_openid_rfb[account_openid][0]:
                    account_openid_rfb[account_openid][0] = read_num
                    account_openid_rfb[account_openid][1] = yuedu_fensi_bi
                else:
                    pass
            #fensi = read_num / yuedu_fensi_bi
            #yfb = str(read_num) +"_"+ str(yuedu_fensi_bi) +"_"+ str(fensi)
            #account_openid_rfb[account_openid].append(yfb)
        # end for
        #print "END statistic in mongodb...%s" %time.strftime("%Y-%m-%d %H:%M:%S")


def write_statistic(file_out):
    #global OUTPUT only use just use it ;do not need to global
    with open(file_out,"w") as fw:
        for open_id,open_id_list in account_openid_rfb.items():
                fw.write(open_id +"\t"+ str(open_id_list[0]) +"\t"+ str(open_id_list[1]) +"\t"+ str(int(open_id_list[0]/open_id_list[1])) +"\n")

import traceback
def main(file_in,file_out): # the main function
    try:
        statistic_ydb(file_in)
        write_statistic(file_out)
    except:
        print "ERROR"
        traceback.print_exc()


if (__name__ == "__main__"):
    if len(sys.argv) < 3:
        print "ERROR...argv"
        exit(1)
    main(sys.argv[1],sys.argv[2])
