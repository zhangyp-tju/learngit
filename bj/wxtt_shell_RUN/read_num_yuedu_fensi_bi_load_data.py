#!/usr/bin/python
#-*-encoding:utf-8-*-

import sys
import pymongo
import time
from datetime import datetime


SOURCE_IP = "10.136.20.106" # mongodb IP
SOURCE_PORT = 27070 # mongodb PORT
openid_set = set()

# connect the mongodb and find return the cursor
def inner_get_conn():

    return pymongo.Connection(host=SOURCE_IP,port=SOURCE_PORT)

def inner_get_cursor(conn,db_name,coll_name,LOW,HIGH):
    #conditions = {"page_time":{"$gt":LOW},"page_time":{"$lt":HIGH}}
    conditions = {"account_openid":{"$in":list(openid_set)},"page_time":{"$gt":LOW,"$lt":HIGH}}
    selects = {"account_openid":1,"page_time":1,"read_num":1,"yuedu_fensi_bi":1}
    #print conditions,selects
    #db_src_article = conn_src.WeiXinRecom.weixin_articles # sorurce DB # db = conn_src['WeiXinRecom']['weixin_articles']
    db = conn[db_name][coll_name]#.WeiXinRecom.weixin_articles # sorurce DB # db = conn_src['WeiXinRecom']['weixin_articles']
    return db.find(conditions,selects)#.sort('account_openid',pymongo.ASCENDING)#.limit(10000).count()#pymongo is sensitive '',True not true
    # write the rusults


# read mongodb one by one and statistic
def statistic_mongodb(file_out,st,end):
    #openid, account, topic1, sutopic_1, total_num, topic_num , subtopic_num  对每一个topic1, 按照 subtopic_num排序$
    conn_src = inner_get_conn()
    cursor = inner_get_cursor(conn_src,'WeiXinRecom','weixin_articles',st,end) # call function$
    # read DBs
    with open(file_out,'w') as fpw:
        for datadic in cursor:
            account_openid = datadic.get("account_openid","")
            page_time = datadic.get("page_time",0)
            read_num = datadic.get("read_num",0)
            yuedu_fensi_bi = datadic.get("yuedu_fensi_bi",0)
            #page_time_str = datetime.fromtimestamp(int(page_time)).strftime("%Y%m%d %H:%M:%S")
            fpw.write(account_openid +"\t"+ str(page_time)  +"\t"+ str(read_num)  +"\t"+ str(yuedu_fensi_bi) + "\n" )

        conn_src.close()

import traceback

def load_data_from_mongo(file_out,st,end): # the main function
    print "BEGIN STATISTIC"
    try:
        statistic_mongodb(file_out,st,end)
    except:
        print "ERROR"
        traceback.print_exc()
    print "END STATISTIC"

# add by zyp
def load_openid(openid_file):
    with open(openid_file) as fpr:
        for line in fpr:
            line = line.strip()
            if not line:continue
            openid_set.add(line)

def data2ts(st,end):
    data_start = st + " 00:00:00"
    data_end = end + " 23:59:59"
    st_tuple = time.strptime(data_start, "%Y%m%d %H:%M:%S")
    end_tuple = time.strptime(data_end, "%Y%m%d %H:%M:%S")
    return int(time.mktime(st_tuple)),int(time.mktime(end_tuple))

def main():
    if len(sys.argv) < 4:
        print "ERROR avgv"
        exit(1)
    load_openid(sys.argv[1])
    data_start,data_end = data2ts(sys.argv[3],sys.argv[4])
    print data_start,data_end
    load_data_from_mongo(sys.argv[2],data_start,data_end)


if (__name__ == "__main__"):
    main()
