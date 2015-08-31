#!/usr/bin/python2.6
#coding=utf-8

import sys
import os
import time

open_id_dic = {}
DEBUG = 0
LOW = 1439135999
HIGH = 1439395199

import json

# 1439135999 ~ 1439395199  _id "account_openid":1,"page_time":1,"read_num":1,"yuedu_fensi_bi":1
def statistic_by_time_json_old(file_in,file_out):
    with open(file_in,'a') as fw:
        dataDict_list = json.load(fw) # 一次性全部读进来，跟无buffer的fread是一样的 因此越发的感觉，json保留数据库的中间结果不靠谱，不如直接用python操作mongon库
        for datadic in dataDict_list:
            #print datadic
            for key,value in datadic.items():
                print "***%s : %s" % (key,value)

from datetime import datetime

def write_one_statistic(open_id,open_id_list,file_out):
    with open(file_out,"a") as fw:
        fw.write(open_id +","+ ",".join(open_id_list) + "\n")

# 1439135999 ~ 1439395199  _id "account_openid":1,"page_time":1,"read_num":1,"yuedu_fensi_bi":1
def statistic_by_time_json(file_in,file_out):
    flag = 1
    with open(file_in,'r') as fw:
        open_id_list = []
        dataDict_list = json.load(fw) # 一次性全部读进来，跟无buffer的fread是一样的 因此越发的感觉，json保留数据库的中间结果不靠谱，不如直接用python操作mongon库
        for datadic in dataDict_list:
            if flag:
                p_account_openid = datadic.get("account_openid","")
                print p_account_openid
                flag = 0
            account_openid = datadic.get("account_openid","")
            page_time = datadic.get("page_time",0)
            read_num = datadic.get("read_num",0)
            yuedu_fensi_bi = datadic.get("yuedu_fensi_bi",0)
            #page_time_str = datetime.fromtimestamp(int(page_time)).strftime("%Y%m%d %H:%M:%S")
            if page_time<LOW or page_time>HIGH or 0==read_num or 0==yuedu_fensi_bi:
                continue
            elif p_account_openid != account_openid:
                #print account_openid
                p_account_openid = account_openid
                if len(open_id_list) < 1:
                    continue
                #print account_openid,p_account_openid
                write_one_statistic(account_openid,open_id_list,file_out)
                del open_id_list[:]

            else:
                fensi = read_num / yuedu_fensi_bi
                yfb = str(read_num) +"_"+ str(yuedu_fensi_bi) +"_"+ str(fensi)
                open_id_list.append(yfb)



def test_dump_json():
    dic_list = []
    fp = file("./test.json",'w')
    for i in range(1,10):
        dic_data = {}
        dic_data["name"] = i
        dic_data["age"] = i
        dic_list.append(dic_data)
    json.dump(dic_list,fp)

# need two args: first for dir_src second for file_path ()
def main_statistic_openid_timestamp():
    current_path = os.getcwd()
    print "参数0：%s" % (sys.argv[0])
    if len(sys.argv) < 6:
        print >> sys.stderr,"ERROR CMD(main_statistic_openid_timestamp)...Usage:tatistic_fawen_byopenid.py [FOLDER_SRC] [FILE_OUT]"
        exit(1)
    dir_path = os.path.join(current_path,sys.argv[1])
    out_path = os.path.join(current_path,sys.argv[5])
    print "START: %s ---- statistic in mongodb...%s" % (dir_path,time.strftime("%Y-%m-%d %H:%M:%S"))
    statistic_by_time_json(sys.argv[1],out_path) # this is the main function
    print "END: %s ---- statistic in mongodb...%s" % (dir_path,time.strftime("%Y-%m-%d %H:%M:%S"))
    statistic_by_time_json(sys.argv[2],out_path) # this is the main function
    print "END: %s ---- statistic in mongodb...%s" % (sys.argv[2],time.strftime("%Y-%m-%d %H:%M:%S"))
    statistic_by_time_json(sys.argv[3],out_path) # this is the main function
    print "END: %s ---- statistic in mongodb...%s" % (sys.argv[3],time.strftime("%Y-%m-%d %H:%M:%S"))
    statistic_by_time_json(sys.argv[4],out_path) # this is the main function
    print "END: %s ---- statistic in mongodb...%s" % (sys.argv[4],time.strftime("%Y-%m-%d %H:%M:%S"))

    test_dump_json()

# python2.6 read_num_yuedu_fensi_bi.py ./read_num_yuedu_fensi_bi.txt final_out.csv
if __name__ == "__main__":
    main_statistic_openid_timestamp()
