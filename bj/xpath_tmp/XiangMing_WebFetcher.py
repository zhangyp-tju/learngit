#coding=gbk
import os
import sys
import httplib
import time
import re
import multiprocessing
import urllib
import traceback
from conf import GlobalConfig
from conf import SeedConf
from lib import Util
from lib import URLExtractor
from lib import URLReposityClient
from lib import WebSpider
from template import xpath as XPATH
import MySQLdb

ue = URLExtractor.URLExtractor(None)
DBName="weixin_news"
TableName="doc_table"
SeedTable = "seed_table"

def ConnectMySQL():
    try:
        wx_conn = MySQLdb.connect(host="10.134.30.154",user="root",passwd="root",db="weixin_news",port=3306,charset="gbk")
        wx_conn.ping(True)
        return wx_conn
    except MySQLdb.Error,e:
        print >> sys.stderr,"[InitMySQL] wxMySQL Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)


def load_seed(start_time):
    global wx_cur
    sql = 'select title,docid from doc_table where time > %s'
    params = (start_time)
    wx_cur.execute(sql,params)
    res = wx_cur.fetchall()
    count = 0
    for r in res:
        count += 1
        #if count>2:break
        seed = SeedConf.NewsScoreSeed(r[0], r[1])
        SeedConf.SEED_LIST.append(seed)
    print count
    print "Load %d Seed" %(len(SeedConf.SEED_LIST))
def add_db(baidu_score, seed):
    global wx_cur
    sql = "update doc_table set baidu_score = %s where docid = %s"
    params = (baidu_score,seed.docid)
    wx_cur.execute(sql,params)

def purify(title):
    title = title.split('\n')[0]
    return title

def analysis_doc(doc, host, seed, client, domain="baidu"):
    charset = ue.getCharset(doc)
    print host, "Charset", charset, len(doc)
    if host.find('tech.qq.com') != -1:
        charset = 'gbk'

    now_xpath = r"//span[@class='c-info']/a[@class='c-more_link']"
    node_list = XPATH.parse(doc, now_xpath, charset)
    res = 0
    prev = 100000
    for node in node_list:
        #'''
        node_val = int(node.text[:-5])
        #if node_val > prev:
        #    break
        res += node_val
        #prev = node_val
        #'''
        #print node.text.encode('gbk')
    return res


def filter_doc(doc):
    if len(doc) < 10:
        return True
    return False

#pageQue.put("http://www.baidu.com/qq", block=True)
def g_Fetch(seedQue, detailQue, pid):
    count = 0
    client = URLReposityClient.URLReposityClient()
    client.ChangeDB(GlobalConfig.PAGE_DB_NUM)
    while (True):
        count += 1
        if seedQue.empty():
            #print "empty"
            break
        #empty last for 2 mins, indicates task ends
        #print "URLQUE SIZE %d" %(seedQue.qsize())
        seed = seedQue.get(block=False)
        if seed is None:
            break
        host, url, tag = None, None, None
        try:
            host, uri = WebSpider.getHost(seed.baidu_url)
        except:
            traceback.print_exc()
            print "Parse URL ERROR"
            continue
        doc, status = WebSpider.URLRequest(host, uri, retry_num = 3)
        if uri == "":
            uri = "/"
        #print "Process Page Query %s(%s|%s)%d" %(seed.title.encode('gbk'), host, uri, status)
        if filter_doc(doc):
            continue
        try:
            baidu_score = analysis_doc(doc, host, seed, client)
            #print "Baidu score of %s is %s" %(seed.title.encode('gbk'),baidu_score)
            add_db(baidu_score, seed)
        except:
            traceback.print_exc()
            print "analysis %s error" %(seed.baidu_url)
        #pageQue.put(r)
        time.sleep(GlobalConfig.INTERVAL)


class WebFetcher:
    def __init__(self, conf):
        self.conf = conf
    def __init__(self):
        self.conf = {}
        self.conf["ProcessNum"] = 10

    def Run(self):
        self.processQueue = []
        mgr = multiprocessing.Manager()
        seedQue = multiprocessing.Queue(1000000)
        detailQue = multiprocessing.Queue(1000000)
        picQue = multiprocessing.Queue(1000000)
        for seed in SeedConf.SEED_LIST:
            seedQue.put(seed, block=True)
        pid = 0
        for i in range(0, 10):
            process = multiprocessing.Process(target=g_Fetch, args=(seedQue, detailQue, i))
            self.processQueue.append(process)

        print "create %d process" %(len(self.processQueue))
        for i in range(0, len(self.processQueue)):
            self.processQueue[i].start()
        for i in range(0, len(self.processQueue)):
            self.processQueue[i].join()
        print "Finished Total Complete %d" %(1000)

def usage():
    print "Usage : python WebFetcher.py modual_name(xinhua, ifeng or 163)"

if __name__=='__main__':

    global wx_cur
    wx_conn = ConnectMySQL()
    wx_cur = wx_conn.cursor()
    load_seed(sys.argv[1])
    fetcher = WebFetcher()
    fetcher.Run()
    wx_conn.close()
