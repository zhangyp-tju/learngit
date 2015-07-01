#!/usr/bin/python
#-*-encoding:utf-8-*-

import hashlib
import pymongo

MAX_SUBTPIC = 2000
account_openid_weight = {}

def garry_statistics():
    #openid, account, topic1, sutopic_1, total_num, topic_num , subtopic_num  对每一个topic1, 按照 subtopic_num排序
    print "in garry"
    SOURCE_IP = "10.144.85.109"
    SOURCE_PORT = 17016
    conn_src = pymongo.Connection(host=SOURCE_IP,port=SOURCE_PORT)
    #db_src_article = conn_src.WeiXinRecom.weixin_articles# sorurce DB
    db_src_article = conn_src.WeiXinRecom.weixin_articles # sorurce DB
    res_arts = db_src_article.find({},{"topic1":1,"subtopic_1":1,"account_openid":1,"account":1})#.limit(10000)#pymongo is sensitive '',True not true
    topic1_account_openid_subtopic_1_num = {}
    account_openid_num = {}
    
    cnt_topic1 = 0
    cnt_subtopic_1 = 0
    # read DBs
    for art in res_arts:
        topic1 = art.get('topic1',"kong top")
        subtopic_1 = art.get('subtopic_1','kong sub')
        account_openid = art.get('account_openid','kong acc_op')
        account = art.get('account','kong acc')
        account_openid += ("\t" + account)
        if not topic1:
            topic1 = "others"
            cnt_topic1 += 1
        if not subtopic_1:
            subtopic_1 = "sub_others"
            cnt_subtopic_1 += 1
        # statistic
        if topic1 not in topic1_account_openid_subtopic_1_num:
            topic1_account_openid_subtopic_1_num[topic1] = {}
            if account_openid not in topic1_account_openid_subtopic_1_num[topic1]:
                topic1_account_openid_subtopic_1_num[topic1][account_openid] = {}
                if subtopic_1 not in topic1_account_openid_subtopic_1_num[topic1][account_openid]:
                    topic1_account_openid_subtopic_1_num[topic1][account_openid][subtopic_1] = 1
                else:
                    topic1_account_openid_subtopic_1_num[topic1][account_openid][subtopic_1] += 1
            else:
                if subtopic_1 not in topic1_account_openid_subtopic_1_num[topic1][account_openid]:
                    topic1_account_openid_subtopic_1_num[topic1][account_openid][subtopic_1] = 1
                else:
                    topic1_account_openid_subtopic_1_num[topic1][account_openid][subtopic_1] += 1
               
        else:
            if account_openid not in topic1_account_openid_subtopic_1_num[topic1]:
                topic1_account_openid_subtopic_1_num[topic1][account_openid] = {}
                if subtopic_1 not in topic1_account_openid_subtopic_1_num[topic1][account_openid]:
                    topic1_account_openid_subtopic_1_num[topic1][account_openid][subtopic_1] = 1
                else:
                    topic1_account_openid_subtopic_1_num[topic1][account_openid][subtopic_1] += 1
            else:
                if subtopic_1 not in topic1_account_openid_subtopic_1_num[topic1][account_openid]:
                    topic1_account_openid_subtopic_1_num[topic1][account_openid][subtopic_1] = 1
                else:
                    topic1_account_openid_subtopic_1_num[topic1][account_openid][subtopic_1] += 1

        # statistic by account_openid
        account_openid_num[account_openid] = account_openid_num.get(account_openid,0) + 1
    # end for
    conn_src.close()
    # write the rusults
    fw = open("statistics_0630newnew.data","w")
    print >> fw, "account_openid\taccount\ttopic1\tsubtopic_1\ttotal_num\ttopic1_value\tsubtopic_1_value"
    for topic1, topic1_value in topic1_account_openid_subtopic_1_num.items():
        subtopic_1_value_temp = {} # rebuild the key value
        for account_openid, account_openid_value in topic1_value.items():
            topic1_value = sum(account_openid_value.values())
            for subtopic_1, subtopic_1_value in account_openid_value.items():
                key = "%s\t%s\t%s\t%d\t%d" % \
                    (account_openid,topic1,subtopic_1,account_openid_num[account_openid],\
                    topic1_value)
                subtopic_1_value_temp[key] = subtopic_1_value#end for subtopic_1 and account_openid
        subtopic_1_value_sort = sorted(subtopic_1_value_temp.items(), key=lambda d:d[1], reverse=True)

        subtopic_1_cnt = 0
        for key, key_value in subtopic_1_value_sort:
            subtopic_1_cnt += 1
            if subtopic_1_cnt > MAX_SUBTPIC:
                break
            account_openid = key.strip().split('\t',1)[0]
            account_openid_weight_values = account_openid_weight.get(account_openid,'')
            #print account_openid
            print >> fw, ("%s\t%d\t%s") % (key, key_value, account_openid_weight_values)

    # end for
    fw.close()

def init_load_account_weight():
    print "BEGIN init_load_account_weight..."
    with open("./account_weight.mysql",'r') as fr:
        for line in fr:
            fields = line.strip().split("\t",1)
            account_openid_weight[fields[0]] = fields[1]
    print "END init_load_account_weight..."


if (__name__ == "__main__"):
    init_load_account_weight()
    garry_statistics()
