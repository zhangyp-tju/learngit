#!/usr/bin/python2.6
#coding=gbk
import os
import sys
import httplib
import time
import re
import multiprocessing
import urllib
import traceback
import xpath as XPATH
import MySQLdb

def ConnectMySQL():
    try:
        wx_conn = MySQLdb.connect(host="10.134.30.154",user="root",passwd="root",db="weixin_news",port=3306,charset="gbk")
        wx_conn.ping(True)
        return wx_conn
    except MySQLdb.Error,e:
        print >> sys.stderr,"[InitMySQL] wxMySQL Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)


def load_seed():
    global wx_cur
    #sql = 'select title,docid from doc_table where time > %s'
    sql = 'select template_path,url from seed_table'
    wx_cur.execute(sql)
    res = wx_cur.fetchall()
    count = 0
    for r in res:
        count += 1
        if count>2:
            #XPATH.test('http://news.163.com/mobile/', '//div/section//a', "gbk")
            XPATH.test('http://zhengwu.beijing.gov.cn/gzdt/', '//body/div[3]/div[2]/div[3]//a', "gbk")
            break
        #print type(r),r
        url = str(r[1])
        xpath = str(r[0])
        print "***cnt:%s url:%s xpath:%s"  % (count,url,xpath)
        XPATH.test(url, xpath, "gbk")
    print count



if __name__=='__main__':

    global wx_cur
    wx_conn=ConnectMySQL()
    wx_cur = wx_conn.cursor()
    load_seed()
    wx_conn.close()
