#!/usr/bin/python
#-*-encoding:utf-8-*-

import hashlib
import pymongo
import time

MAX_SUBTPIC = 2000
account_openid_weight = {} # use in the init_load_account_weight function 


OUTPUT = "d_statistic.csv" # OUTPUT filename
SOURCE_IP = "10.144.85.109" # mongodb IP
SOURCE_PORT = 17016   # mongodb PORT


topic1_account_openid_subtopic_1_num = {} # the main dicts
account_openid_num = {} # all the subtopic_1 by account_openid


# connect the mongodb and find return the cursor
def inner_get_conn():

    return pymongo.Connection(host=SOURCE_IP,port=SOURCE_PORT)

def inner_get_cursor(conn,db_name,coll_name):
    
    conditions = {"topic1":1,"subtopic_1":1,"account_openid":1,"account":1,"read_num":1,"app_click_num":1,\
        "app_show_num":1,"app_share_num":1,"app_favor_num":1}
    #db_src_article = conn_src.WeiXinRecom.weixin_articles # sorurce DB # db = conn_src['WeiXinRecom']['weixin_articles']
    db = conn[db_name][coll_name]#.WeiXinRecom.weixin_articles # sorurce DB # db = conn_src['WeiXinRecom']['weixin_articles']
    return db.find({},conditions)#.limit(10000)#pymongo is sensitive '',True not true

def inner_statistic_sub_ALL(topic1,account_openid,subtopic_1,read_num,app_click_num,app_show_num,app_share_num,app_favor_num):
    # the argument sutopic_1 is non using
    topic1_account_openid_subtopic_1_num[topic1][account_openid]['ALL']['cnt'] = \
        topic1_account_openid_subtopic_1_num[topic1][account_openid]['ALL'].get('cnt',0) + 1
    topic1_account_openid_subtopic_1_num[topic1][account_openid]['ALL']['total_read_num'] = \
        topic1_account_openid_subtopic_1_num[topic1][account_openid]['ALL'].get('total_read_num',0) + read_num 
    topic1_account_openid_subtopic_1_num[topic1][account_openid]['ALL']['app_click_num'] = \
        topic1_account_openid_subtopic_1_num[topic1][account_openid]['ALL'].get('app_click_num',0) + app_click_num
    topic1_account_openid_subtopic_1_num[topic1][account_openid]['ALL']['app_show_num'] = \
        topic1_account_openid_subtopic_1_num[topic1][account_openid]['ALL'].get('app_show_num',0) + app_show_num
    topic1_account_openid_subtopic_1_num[topic1][account_openid]['ALL']['app_share_num'] = \
        topic1_account_openid_subtopic_1_num[topic1][account_openid]['ALL'].get('app_share_num',0) + app_share_num
    topic1_account_openid_subtopic_1_num[topic1][account_openid]['ALL']['app_favor_num'] = \
        topic1_account_openid_subtopic_1_num[topic1][account_openid]['ALL'].get('app_favor_num',0) + app_favor_num

def inner_statistic_subtopic_1(topic1,account_openid,subtopic_1,read_num,app_click_num,app_show_num,app_share_num,app_favor_num):
    topic1_account_openid_subtopic_1_num[topic1][account_openid][subtopic_1]['cnt'] = \
        topic1_account_openid_subtopic_1_num[topic1][account_openid][subtopic_1].get('cnt',0) + 1
    topic1_account_openid_subtopic_1_num[topic1][account_openid][subtopic_1]['total_read_num'] = \
        topic1_account_openid_subtopic_1_num[topic1][account_openid][subtopic_1].get('total_read_num',0) + read_num
    topic1_account_openid_subtopic_1_num[topic1][account_openid][subtopic_1]['app_click_num'] = \
        topic1_account_openid_subtopic_1_num[topic1][account_openid][subtopic_1].get('app_click_num',0) + app_click_num
    topic1_account_openid_subtopic_1_num[topic1][account_openid][subtopic_1]['app_show_num'] = \
        topic1_account_openid_subtopic_1_num[topic1][account_openid][subtopic_1].get('app_show_num',0) + app_show_num
    topic1_account_openid_subtopic_1_num[topic1][account_openid][subtopic_1]['app_share_num'] = \
        topic1_account_openid_subtopic_1_num[topic1][account_openid][subtopic_1].get('app_share_num',0) + app_share_num
    topic1_account_openid_subtopic_1_num[topic1][account_openid][subtopic_1]['app_favor_num'] = \
        topic1_account_openid_subtopic_1_num[topic1][account_openid][subtopic_1].get('app_favor_num',0) + app_favor_num

def inner_statistic(topic1,account_openid,subtopic_1,read_num,app_click_num,app_show_num,app_share_num,app_favor_num):
    common_args_sub = (topic1,account_openid,subtopic_1,read_num,app_click_num,app_show_num,app_share_num,app_favor_num)
    if account_openid not in topic1_account_openid_subtopic_1_num[topic1]:
        topic1_account_openid_subtopic_1_num[topic1][account_openid] = {}
        topic1_account_openid_subtopic_1_num[topic1][account_openid]['ALL'] = {}# create is very important...
        #subtopic_1 = 'ALL'
        inner_statistic_sub_ALL(*common_args_sub)

        if subtopic_1 not in topic1_account_openid_subtopic_1_num[topic1][account_openid]:
            topic1_account_openid_subtopic_1_num[topic1][account_openid][subtopic_1] = {}

            inner_statistic_subtopic_1(*common_args_sub)

        else:
            inner_statistic_subtopic_1(*common_args_sub)
            
    else:
        #topic1_account_openid_subtopic_1_num[topic1][account_openid]['ALL'] = {}
        inner_statistic_sub_ALL(*common_args_sub)
                       
        if subtopic_1 not in topic1_account_openid_subtopic_1_num[topic1][account_openid]:
            topic1_account_openid_subtopic_1_num[topic1][account_openid][subtopic_1] = {}
            
            inner_statistic_subtopic_1(*common_args_sub)
            
        else:
            inner_statistic_subtopic_1(*common_args_sub)


# read mongodb one by one and statistic
def statistic_mongodb():
    #openid, account, topic1, sutopic_1, total_num, topic_num , subtopic_num  对每一个topic1, 按照 subtopic_num排序$
    print "BEGIN STATISTIC(starting in mongodb)...%s" %time.strftime("%Y-%m-%d %H:%M:%S")
    conn_src = inner_get_conn()
    res_arts = inner_get_cursor(conn_src,'WeiXinRecom','weixin_articles') # call function$
    # read DBs
    for art in res_arts:
        topic1 = art.get('topic1',"kong top")
        subtopic_1 = art.get('subtopic_1','kong sub')
        account_openid = art.get('account_openid','kong acc_op')
        account = art.get('account','kong acc')
        read_num = art.get('read_num',0)
        account_openid += ("," + account)
        app_click_num = art.get('app_click_num',0)
        app_show_num = art.get('app_show_num',0)
        app_share_num = art.get('app_share_num',0)
        app_favor_num = art.get('app_favor_num',0)

        common_args = (topic1,account_openid,subtopic_1,read_num,app_click_num,app_show_num,app_share_num,app_favor_num)

        if not topic1 or topic1 == "others":
            topic1 = "others"
            continue
        if not subtopic_1 or subtopic_1=="NULL" or subtopic_1 == "other":
            subtopic_1 = "sub_others"
            continue

        # statistic  avenue_read_num the main oprerations
        if topic1 not in topic1_account_openid_subtopic_1_num:
            topic1_account_openid_subtopic_1_num[topic1] = {}

            inner_statistic(*common_args)

        else:
            inner_statistic(*common_args)
        # statistic only by account_openid
        account_openid_num[account_openid] = account_openid_num.get(account_openid,0) + 1
    # end for
    conn_src.close()
    print "END statistic in mongodb...%s" %time.strftime("%Y-%m-%d %H:%M:%S")


def inner_calc_res(subtopic_1_value):
    # calculate the avg_read_num
    cnt = subtopic_1_value['cnt']
    if not cnt:
        cnt = 1
    avg_read_num = subtopic_1_value['total_read_num'] / cnt
    #calculate the CTR
    app_click_num = subtopic_1_value['app_click_num']
    app_show_num = subtopic_1_value['app_show_num']
    app_share_num = subtopic_1_value['app_share_num']
    app_favor_num = subtopic_1_value['app_favor_num']
    attr_four = "None"
    if (app_click_num + app_show_num + app_share_num + app_favor_num) == 0:pass
    else:
        attr_four = str(app_click_num) + "/" + str(app_show_num) + "/" + str(app_share_num) + "/" + str(app_favor_num)
    if not app_show_num:
        app_show_num = 1
    CTR = (app_click_num + app_share_num + app_favor_num) * 1.0 / app_show_num

    return cnt, avg_read_num, attr_four,CTR


# write_results
def statistic_write_results():
    # write the rusults
    print "***BEGIN writting results...%s" %time.strftime("%Y-%m-%d %H:%M:%S")
    title_tips = "account_openid,account,topic1,subtopic_1,total_num,topic1_value,avg_read_num,ck_sw_se_fr,CTR,subtopic_1_value,zhu_weigh    t,cong_weight,account_weight,topic1_url,subtopic_1_url"
    print "BEGIN in write_results..."
    fw = open(OUTPUT,"w")

    print >> fw,title_tips #the first line  in excel 

    for topic1, topic1_values in topic1_account_openid_subtopic_1_num.items():
        #topic_all = topic1_num[topic1]
        subtopic_1_value_temp = {} # rebuild the key value
        for account_openid, account_openid_value in topic1_values.items():
            topic1_value = account_openid_value['ALL']['cnt']
            for subtopic_1, subtopic_1_value in account_openid_value.items():
                # calc_res calculate function
                cnt, avg_read_num, attr_four,CTR = inner_calc_res(subtopic_1_value)
                
                key = "%s,%s,%s,%d,%d,%d,%s,%.4f" % \
                    (account_openid,topic1,subtopic_1,account_openid_num[account_openid],topic1_value,avg_read_num,attr_four,CTR)
                subtopic_1_value_temp[key] = cnt#end for subtopic_1 and account_openid

        # end for the second for and sort by cnt
        subtopic_1_value_sort = sorted(subtopic_1_value_temp.items(), key=lambda d:d[1], reverse=True)

        subtopic_1_cnt = 0 # count the rusults and just get the above
        for key, key_value in subtopic_1_value_sort:
            subtopic_1_cnt += 1
            if subtopic_1_cnt >= MAX_SUBTPIC:
                break
            # original DBs
            key_eles = key.strip().split(',')
            account_openid= key_eles[0]
            topic1 = key_eles[2]
            subtopic_1 = key_eles[3]

            topic1_url,subtopic_1_url = inner_quote_urls(account_openid,topic1,subtopic_1)#call for function

            # from file of ./account_weight.mysql
            account_openid_weight_values = account_openid_weight.get(account_openid)
            if not account_openid_weight_values:# bu qi
                account_openid_weight_values = "zhu\t0\tcong\t0"
            # from file
            account_openid_weight_values_eles = account_openid_weight_values.split('\t')
            if len(account_openid_weight_values_eles) < 4:
                print account_openid_weight_values
                continue
            topic1_file_value_bk = account_openid_weight_values_eles[1]
            subtopic_1_file_value_bk = account_openid_weight_values_eles[3]

            account_openid_weight_values = inner_get_weights_str(topic1,subtopic_1,account_openid_weight_values_eles)

            #print account_openid
            print >> fw, ("%s,%d,%s,%s,%s,%s,%s") \
                % (key, key_value, topic1_file_value_bk,subtopic_1_file_value_bk,account_openid_weight_values,topic1_url,subtopic_1_url)
    # end for
    fw.close()
    print "END write_results...%s" %time.strftime("%Y-%m-%d %H:%M:%S")

import urllib
def inner_quote_urls(account_openid,topic1,subtopic_1):
    pre_url = "http://10.134.37.33:8889/"
    topic1_encode = urllib.quote(topic1.decode('gbk').encode('utf-8'))
    #print topic1_encode
    topic1_url = pre_url + "zhu_cong_account?account_openid="  + account_openid + "&zhu=" + topic1_encode#.decode('gbk') 
    subtopic_1_encode = urllib.quote(subtopic_1.decode('gbk').encode('utf8'))
    subtopic_1_url = topic1_url + "&cong=" + subtopic_1_encode#.decode('gbk')
    return topic1_url,subtopic_1_url

def inner_get_weights_str(topic1,subtopic_1,account_openid_weight_values_eles):
    topic1_file = account_openid_weight_values_eles[0]
    topic1_file_value = account_openid_weight_values_eles[1]
    subtopic_1_file = account_openid_weight_values_eles[2]
    subtopic_1_file_value = account_openid_weight_values_eles[3]
    if not topic1_file:
        topic1_file = "zhu"
        topic1_file_value = "0"
    elif topic1_file != topic1:
        topic1_file_value = "0"
    else:
        pass
    
    if subtopic_1 == 'ALL':
        subtopic_1_file = ""
        subtopic_1_file_value = ""
    elif not subtopic_1_file:
        subtopic_1_file = "cong"
        subtopic_1_file_value = "0"
    elif subtopic_1_file != subtopic_1:
        subtopic_1_file_value = "0"
    
    else:
        pass
        #print account_openid_weight_values
    return (topic1_file +"_" + topic1_file_value + "-" + subtopic_1_file + "_" + subtopic_1_file_value)


def garry_statistics(): # the main function 
    #openid, account, topic1, sutopic_1, total_num, topic_num , subtopic_num  对每一个topic1, 按照 subtopic_num排序
    print "BEGIN STATISTIC"
    statistic_mongodb()
    # write the rusults
    statistic_write_results()
    print "END STATISTIC"

def init_load_account_weight():
    print "BEGIN init_load_account_weight..."
    with open("./account_weight.mysql",'r') as fr:
        for line in fr:
            fields = line.strip().split("\t",1)
            #print fields[0],fields[1][:-1],fields[1]
            account_openid_weight[fields[0]] = fields[1].strip()
    print "END init_load_account_weight..."


if (__name__ == "__main__"):
    init_load_account_weight()
    garry_statistics()
