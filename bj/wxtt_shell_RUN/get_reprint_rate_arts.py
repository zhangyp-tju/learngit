#!/usr/bin/env python
# coding=utf-8

import sys
import time
import logging
import urllib2
import urllib
import multiprocessing
import httplib
from datetime import datetime
import pymongo


timeValue = time.strftime('%Y-%m-%d',time.localtime(time.time()))
LOG_FILE = 'log/' + timeValue
#TOPN = 100

open_id_reprint = {} # 对应三个值 用list?dict?
openid_set = set()

def inner_get_cursor():
    db_ip = "10.136.20.106"
    db_port = 27070
    db_name = "WeiXinEvent"
    t_name = "wx_signature_invinfo"
    conditions = {"account_openid":{"$in":list(openid_set)}}
    #conn = pymongo.connection.Connection(host = db_ip,port = db_port)
    conn = pymongo.Connection(host = db_ip,port = db_port)
    db = conn[db_name][t_name]
    #return db.find({"total_num" : 3}).limit(100)
    return db.find(conditions)#.limit(10000)
def inner_parse(art):
    new_art = {}
    try:
        new_art['ArticlesInfoList'] = art.get('ArticlesInfoList',None) # list of open_id for the same Event
        new_art['_id'] = art.get('_id',None) # Event id
        new_art['total_num'] = art.get('total_num',None) # numbers of open_id for the same Event
    except:
        print "ERROR..."
    #print new_art
    return new_art

def inner_get_original_arts_cnt(articlesInfoList):
    ori_open_id = "" # account_openid page_time  url
    ori_url = ""
    ori_page_time = time.time()
    for index in range(0,len(articlesInfoList)): # 取得最小的page_time作为原始的发文
        tmp_page_time = articlesInfoList[index].get('page_time',None)
        tmp_account_openid = articlesInfoList[index].get('account_openid',None)
        #tmp_url = articlesInfoList[index].get('url',None)
        #statistic arts for open_id
        open_id_reprint[tmp_account_openid] = open_id_reprint.get(tmp_account_openid,[0,0,0])
        open_id_reprint[tmp_account_openid][1] += 1 # 统计发文篇数（原创 或 转载）

        #assert tmp_page_time > ori_page_time
        if tmp_page_time < ori_page_time:
            #ori_page_time = tmp_page_time
            #ori_url = tmp_url
            ori_open_id = tmp_account_openid

    #return ori_open_id,ori_url,ori_page_time
    return ori_open_id


def statistic_reprint_by_openid():
    for art in inner_get_cursor():
        new_art = inner_parse(art)
        articlesInfoList = new_art['ArticlesInfoList']
        if (len(articlesInfoList) < 2): #虽然是原创，但是未被转载
            account_openid = articlesInfoList[0].get('account_openid',None)
            open_id_reprint[account_openid] = open_id_reprint.get(account_openid,[0,0,0])
            open_id_reprint[account_openid][1] += 1 # 统计发文篇数（原创 或 转载）
        else:
            #ori_open_id,url,pagetime = inner_get_original_arts_cnt(new_art['ArticlesInfoList'])
            ori_open_id = inner_get_original_arts_cnt(articlesInfoList)
            #print inner_get_original_arts_cnt(new_art['ArticlesInfoList'])
            open_id_reprint[ori_open_id] = open_id_reprint.get(ori_open_id) # reprint cnt(对于一个账号的被转载总数),arts_cnt（发文总数）,arts_ori_cnt（原创总数）
            open_id_reprint[ori_open_id][2] += 1 # 仅仅统计被转载n的art_ori_cnt
            open_id_reprint[ori_open_id][0] += new_art['total_num']

# 0--原创被转载的次数 1--发文（转载或原创）文章总数目  2--原创且被转载的文章数目
def write_result(filename):
    with open(filename,'w') as fpw:
        fpw.write('account_openid,rate_reprint,cnt_art(文章总数),cnt_reprint_art(被转载文章数),cnt_reprint(被转载总次数)\n')
        for open_id,v_list in open_id_reprint.items():
            rate_reprint = "%.3f" % (float(v_list[2])/v_list[1])
            fpw.write(open_id +','+ rate_reprint +','+ str(v_list[1]) +','+ str(v_list[2]) +','+ str(v_list[0]-v_list[2]) +'\n' )



def write_result_old(filename):
    with open(filename,'w') as fpw:
        fpw.write('account_openid,rate_reprint,cnt_reprint_art,cnt_reprint,cnt_art\n')
        for open_id,v_list in open_id_reprint.items():
            if (v_list[1] - v_list[2]) == 0:
                print "ERROR ZERO.."
                fpw.write(open_id +','+ '0.000' +','+ str(v_list[2]) +','+ str(v_list[0]) +','+ str(v_list[1]) +'\n' )
            else:
                rate_reprint = "%.3f" % (float(v_list[2])/(v_list[1] - v_list[2]))
                #print open_id ,rate_reprint , str(v_list[2]) , str(v_list[0])
                fpw.write(open_id +','+ rate_reprint +','+ str(v_list[2]) +','+ str(v_list[0]) +','+ str(v_list[1]) +'\n' )

# add by zyp
def load_openid(openid_file):
    with open(openid_file) as fpr:
        for line in fpr:
            line = line.strip()
            if not line:continue
            openid_set.add(line)


if __name__ == '__main__':
    #shell_name = sys.argv[0]
    #out_path = "%s%s%s" % ("./out_results/",shell_name[:-3],".csv")
    if len(sys.argv) < 3:
        print >> sys.stderr, "argv[] ERROR..."
        exit(1)
    load_openid(sys.argv[1])
    out_path = sys.argv[2]
    print "results in file:  %s " % (out_path)
    begin_time = datetime.now()
    # main()
    statistic_reprint_by_openid()
    end_time = datetime.now()
    print 'the cost time of 5statistic_reprint_by_openid is %d s' % ((end_time-begin_time).seconds+0.0)

    write_result(out_path)


