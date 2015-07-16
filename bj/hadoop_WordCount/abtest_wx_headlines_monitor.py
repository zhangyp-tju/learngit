#!/usr/bin/python
#-*-coding:gbk
import os
import sys
import datetime
import time
import pickle
import pdb
import MySQLdb
from WEIXIN_CONST import RESP_LEN,REQ_LEN,PUSH_REQ_LEN

whole_show_map = {}
whole_action_map = {}
whole_click_distribute_map = {}
whole_show_distribute_map = {}
LOG_FLAG="offline"

def string_datetime(input_str):
    try:
        return  int(time.mktime(time.strptime(input_str, "%Y-%m-%d %H:%M:%S")))
    except:
        return 0

        

def get_user_log_req(row):
    (log_type,mid,tm,action,topic,tag,target_title,keywords,userinfo,imsi,target_link,account,channel,flag,OS,openid,ab_test_id,sub_topic) = row[0:REQ_LEN]

    if ab_test_id not in whole_action_map:
        whole_show_map[ab_test_id] = {"show_num":0,"hot_num":0,"rec_num":0,"sticky_thread_show":0,'user_set':set()}
        whole_action_map[ab_test_id] = {"click":0,"hot_click":0,"rec_click":0,"sticky_thread_click":0,"share":0,'user_set':set()}
        whole_click_distribute_map[ab_test_id] = {}
        whole_show_distribute_map[ab_test_id] = {}
    if action == '5' : whole_action_map[ab_test_id]["share"] += 1
   
    if action != '6' and not (action == '8' and OS =='android_3200') :return #zgn add

    if not whole_click_distribute_map[ab_test_id].has_key(topic):
        whole_click_distribute_map[ab_test_id][topic] = 0

    whole_click_distribute_map[ab_test_id][topic] += 1

    if tag == '1':
        whole_action_map[ab_test_id]["hot_click"] += 1
    elif tag == '2':
        whole_action_map[ab_test_id]["rec_click"] += 1
    flag = int(flag)
    if flag%100 == 1:
        whole_action_map[ab_test_id]["sticky_thread_click"] += 1


    whole_action_map[ab_test_id]["click"] += 1
    whole_action_map[ab_test_id]["user_set"].add(mid)

def get_user_log_resp(row):
    #modified by oyb rename type to article_template
    (log_type,mid,tm,article_cnt,num,tag,title,reason,read_num,topic,keywords,pub_time,article_template,\
            img_list,url,account,channel,flag,openid,ab_test_id,sub_topic) = row[0:RESP_LEN]

    if ab_test_id not in whole_action_map:
        whole_show_map[ab_test_id] = {"show_num":0,"hot_num":0,"rec_num":0,"sticky_thread_show":0}
        whole_action_map[ab_test_id] = {"click":0,"hot_click":0,"rec_click":0,"sticky_thread_click":0,"share":0}
        whole_click_distribute_map[ab_test_id] = {}
        whole_show_distribute_map[ab_test_id] = {}



    if not whole_show_distribute_map[ab_test_id].has_key(topic):
        whole_show_distribute_map[ab_test_id][topic] = 0
    whole_show_distribute_map[ab_test_id][topic] += 1

    if tag == '1':
        whole_show_map[ab_test_id]["hot_num"] += 1
    elif tag == '2':
        whole_show_map[ab_test_id]["rec_num"] += 1
    
    flag = int(flag)
    if flag%100 == 1:
        whole_show_map[ab_test_id]["sticky_thread_show"] += 1

    whole_show_map[ab_test_id]["show_num"] += 1
    whole_show_map[ab_test_id]["user_set"].add(mid)

def Dump(cur, start_time, flag_day, if_mysql=False):
    for ab_test_id in whole_action_map:
        total_show_num = whole_show_map[ab_test_id].get("show_num",0)
        total_hot_num = whole_show_map[ab_test_id].get("hot_num",0)
        total_rec_num = whole_show_map[ab_test_id].get("rec_num",0)
        
        total_click = whole_action_map[ab_test_id].get("click",0)
        total_hot_click = whole_action_map[ab_test_id].get("hot_click",0)
        total_rec_click = whole_action_map[ab_test_id].get("rec_click",0)
        
        share_num = whole_action_map[ab_test_id].get("share",0)
        avg_reading_duration = whole_action_map[ab_test_id].get("avg_reading_duration",0.0)
        duration_user_num = whole_action_map[ab_test_id].get("duration_user_num",0)

        #sticky_thread
        st_hot_click_num = 0#whole_action_map["sticky_thread_click"].get(7,0)
        st_rec_click_num = 0#whole_action_map["sticky_thread_click"].get(5,0)
        st_other_click_num = whole_action_map[ab_test_id]["sticky_thread_click"]#.get(1,0)
        total_st_click = st_hot_click_num + st_rec_click_num + st_other_click_num

        st_hot_show_num = 0#whole_show_map["sticky_thread_show"].get(7,0)
        st_rec_show_num = 0#whole_show_map["sticky_thread_show"].get(5,0)
        st_other_show_num = whole_show_map[ab_test_id]["sticky_thread_show"]#.get(1,0)
        total_st_num = st_hot_show_num + st_rec_show_num + st_other_show_num

        user_alive_day = len(whole_show_map[ab_test_id]['user_set'])
        #pickle.dump(whole_show_map[ab_test_id]['user_set'],open('alive'+ab_test_id+'.p','w'))
        click_user_num = len(whole_action_map[ab_test_id]['user_set'])

        click_ctr = 0.0
        hot_ctr = 0.0
        rec_ctr = 0.0
        pv_uv = 0.0
        click_uv = 0.0
        click_user_rate = 0.0
        if user_alive_day != 0:
            click_user_rate = click_user_num * 1.0 / user_alive_day



        #sticky_thread
        st_ctr = 0.0
        st_hot_ctr = 0.0
        st_rec_ctr = 0.0
        st_other_ctr = 0.0

        if total_show_num != 0:
            click_ctr = total_click * 1.0 / total_show_num
            click_ctr = round(click_ctr,4)
        if total_hot_num != 0:
            hot_ctr = total_hot_click * 1.0 / total_hot_num
            hot_ctr = round(hot_ctr, 4)
        if total_rec_num != 0:
            rec_ctr = total_rec_click * 1.0 / total_rec_num
            rec_ctr = round(rec_ctr, 4)
        if total_st_num != 0:
            st_ctr = total_st_click * 1.0 / total_st_num
            st_ctr = round(st_ctr, 4)
        if st_hot_show_num != 0:
            st_hot_ctr = st_hot_click_num * 1.0 / st_hot_show_num
            st_hot_ctr = round(st_hot_ctr, 4)
        if st_rec_show_num != 0:
            st_rec_ctr = st_rec_click_num * 1.0 / st_rec_show_num
            st_rec_ctr = round(st_rec_ctr, 4)
        if st_other_show_num != 0:
            st_other_ctr = st_other_click_num * 1.0 / st_other_show_num
            st_other_ctr = round(st_other_ctr, 4)
        if user_alive_day != 0:
            pv_uv = total_show_num * 1.0 / user_alive_day
            pv_uv = round(pv_uv, 2)
            click_uv = total_click * 1.0 / user_alive_day
            click_uv = round(click_uv, 2)
        output_distribute_list = []
        for topic,value in whole_show_distribute_map[ab_test_id].items():
            tmp_click = whole_click_distribute_map[ab_test_id].get(topic,0)
            tmp_ctr = 0.0
            if value != 0:
                tmp_ctr = tmp_click * 1.0 / value
            tmp_ctr = round(tmp_ctr,4)
            output_distribute_list.append([topic,value,tmp_click,tmp_ctr])

        output_distribute_sort = sorted(output_distribute_list,key=lambda d:d[1],reverse=True)
        output_click_distribute = ""
        for item in output_distribute_sort:
            output_click_distribute += ":".join([str(value) for value in item]) + " "
        output_click_distribute = output_click_distribute.strip()



        if if_mysql == True:
            try:
                sql1 = "insert into wx_headlines_monitor_abtest(op_time,user_alive_day,show_num,click_num,\
                        click_ctr,hot_show_num,hot_click_num,hot_ctr,\
                       rec_num,rec_click_num,rec_ctr,click_distribute,\
                       pv_uv,click_uv,flag_day,log_flag,\
                       click_user_num,click_user_rate,share_num,ab_test_id) values(\
                           %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                
                param1 = (start_time,user_alive_day,total_show_num,total_click,\
                        click_ctr,total_hot_num,total_hot_click,hot_ctr,\
                        total_rec_num,total_rec_click,rec_ctr,output_click_distribute,\
                        pv_uv,click_uv,flag_day,LOG_FLAG,\
                        click_user_num,click_user_rate,share_num,ab_test_id)
                #modify by oyb to test online1 and independ abtest!!
                cur.execute(sql1, param1)   #todo when not testing!
                #if LOG_FLAG == "online1":
                #    cur.execute(sql1, param1)
                #with open("../sqldata_test/wx_headlines_monitor_abtest_" + LOG_FLAG, "a") as fp:
                #    print >> fp, param1
                        
            except MySQLdb.Error,e:
                print >> sys.stderr,"[Dump] MySQL Error %d: %s" % (e.args[0],e.args[1])


def LoadFile(data_file):
    ifp = file(data_file)
    for line in ifp:
        if line.startswith('resp'):
            line = line.strip('\n')
            array = line.split("\t")
            #modify by oyb to cancel length check
            if len(array) < RESP_LEN :
                print >> sys.stderr, "len(array) wrong! %s" % (line)
                continue
            get_user_log_resp(array)
        elif line.startswith('req\t'):
            line = line.strip('\n')
            array = line.split("\t")
            #modify by oyb to cancel length check
            if len(array) < REQ_LEN :
                print >> sys.stderr, "len(array) wrong! %s" % (line)
                continue
            get_user_log_req(array)

    ifp.close()


def main():
    global LOG_FLAG
    start_time = sys.argv[1]

    ##flag_day=1 ÈÕ±¨ flag_day=2 Ã¿Ð¡Ê±½øÐÐÍ³¼Æ
    flag_day = 1
    if len(sys.argv) > 2 and sys.argv[2] == "2":
        flag_day = 2
    if len(sys.argv) > 3:
        LOG_FLAG = sys.argv[3]

    if len(sys.argv) > 4:
        file_name = sys.argv[4]

    try:
        conn = MySQLdb.connect(host='10.134.37.32',user='darrenan',passwd="darrenan",db='db_weixin_abtest',port=3306,charset="gbk")
        cur = conn.cursor()
    except MySQLdb.Error,e:
        print >> sys.stderr,"[main] MySQL Error %d: %s" % (e.args[0],e.args[1])

    LoadFile(file_name)
    Dump(cur,start_time,flag_day,True)

def test():
    global LOG_FLAG
    start_time = '2014-12-26'
    flag_day = 1
    LOG_FLAG = sys.argv[1]

    try:
        conn = MySQLdb.connect(host='10.134.37.32',user='darrenan',passwd="darrenan",db='db_weixin_abtest',port=3306,charset="gbk")
        cur = conn.cursor()
    except MySQLdb.Error,e:
        print >> sys.stderr,"[main] MySQL Error %d: %s" % (e.args[0],e.args[1])
    cmonitor = CMonitor(file_name,flag_day)
    get_user_log_req(cur,start_time,cmonitor)
    get_user_log_resp(cur,start_time,cmonitor)
    #Dump(cur,start_time,flag_day,cmonitor,True)


if __name__ == '__main__':
    main()
    #test()
