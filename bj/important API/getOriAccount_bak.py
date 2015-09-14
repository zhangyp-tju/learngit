#!/usr/bin/env python
# coding=utf-8

import sys
import os
import time
import logging
import urllib2
import urllib
import multiprocessing
import httplib
from datetime import datetime

timeValue = time.strftime('%Y-%m-%d-%H:%M',time.localtime(time.time()))
LOG_FILE = 'log/' + timeValue
#TOPN = 100
ProcessNum = 10

openid_set = set() # for load_openid()
DEBUG = 0
topic_fq = ['搞笑','段子']

def isOriginal(url,openid):
    req_header = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 SE 2.X MetaSr 1.0',
                    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Connection':'keep-alive',
                    'Referer':'http://weixin.sogou.com/gzh?openid=' + openid
                    }
    req_timeout = 15
    try:
        req = urllib2.Request(url,None,req_header)
        response = urllib2.urlopen(req,None,req_timeout)
        html = response.read()
    except:
        sys.stderr.write('find exception ,url:%s \n' % url)
        time.sleep(20)
        return -1
    if  'copyright_stat : "1"' in html: # ori
        return 1
    elif '<em class="rich_media_meta rich_media_meta_text">' in html:# zhuanfa
        return 2
    else:
        return -1 # none


def checkUrl(requestArray,idxArray, lock):
    count = 0
    while(1):
        lock.acquire() # 申请锁
        idx = idxArray[0]
        if idx % 100000 == 0:
            logging.info('crawl lines : %d' % idx)

        if (idx >= idxArray[1]):
            lock.release()
            break # 遍历数组结束
        idxArray[0] = idx + 1
        lock.release() # 释放锁
        url_openid = requestArray[idx]
        cols = url_openid.split('\t')
        try:
            url = cols[0]
            topic = cols[2]
            openid_u_name = cols[-3]
            id_name = openid_u_name.split("##")
            #u_name = id_name[0]
            openid = id_name[1]
        except:
            print >> sys.stderr,"ERROR"
            continue
        if topic in topic_fq:
            continue
        ret = isOriginal(url,openid)
        lock.acquire() # 再次申请锁
        ### output the result...
        if ret > 0:
            print url_openid + '\t' + str(ret)
            sys.stdout.flush()
        lock.release() # 释放锁
# add by zyp load both bad and good openid for filter
def load_openid(openid_file):
    with open(openid_file) as fpr:
        for line in fpr:
            line = line.strip()
            if not line:continue
            openid_set.add(line)

# add by zyp no using
def load_openid_good(openid_file):
    with open(openid_file) as fpr:
        for line in fpr:
            line = line.strip()
            if not line:continue
            openid_good_set.add(line)

def main_judge_orignal(openid_file_bad,openid_file_good,url_dir):
    load_openid(openid_file_bad) ### 垃圾账号
    load_openid(openid_file_good) ### 优质账号
    flag = 1
    if not os.path.isdir(url_dir):
        print >> sys.stderr,"ERROR CMD -- not a dir Usage: statistic_fawen_byopenid.py [FOLDER_SRC] [FILE_OUT]"
        exit(1)
    list_name = os.listdir(url_dir)
    for name in list_name:
        current_path = os.path.join(url_dir,name)
        if os.path.isdir(current_path):
            list_dir(current_path)
        elif os.path.isfile(current_path):
            print >>sys.stderr, "deal with file %s" % current_path
            if flag:
                server_start(current_path) ### 对于每一个file开启一次多线程查询
            if DEBUG:
                flag = 0
### 调用执行 线程
def server_start(url_file):
    begin_time = datetime.now()
    logging.basicConfig(level=logging.DEBUG,format='%(process)d %(asctime)s  %(levelname)s %(message)s',datefmt='%a, %d %b %Y',filename= LOG_FILE,filemode='w')
    processQueue = []
    #invalidUrl = []
    mgr = multiprocessing.Manager()
    idxArray = mgr.list()
    #invalidUrl = mgr.list()
    lock = multiprocessing.Lock()
    idxArray.append(0)
    ### 
    tmpQueryArray = getUrls(url_file) # call fetURLs fun
    ###
    logging.info('all urls is %d' % len(tmpQueryArray))
    requestArray = mgr.list(tmpQueryArray)
    idxArray.append(len(requestArray))
    del tmpQueryArray[0: len(tmpQueryArray)]
    for i in range(0, ProcessNum):
        process = multiprocessing.Process(target=checkUrl, args=(requestArray,idxArray, lock)) # multiprocessing call checkUrl fun
        processQueue.append(process)
    for i in range(0, len(processQueue)):
        processQueue[i].start()
    for i in range(0, len(processQueue)):
        processQueue[i].join()
    end_time = datetime.now()
    logging.info('the cost time is %d s' % ((end_time-begin_time).seconds+0.0) )


# generate one ulrs_list change by zyp
def getUrls(url_file):
    url_list = []
    cnt = 0
    for line in open(url_file):
        if cnt % 100000 == 0:
            logging.info('load url: %d lines' % cnt)
        cnt += 1
        line = line.strip()
        if not line: continue
        cols = line.split("\t")
        if len(cols) != 7:
            continue
        try:
            openid = cols[-3].split("##",1)[1]
        except:
            print >> sys.stderr, "ERROR...%s" % (line)
        #if openid not in openid_set:
        if openid in openid_set: # 优质账号和劣质账号不用判断了
            continue
        url_list.append(line)
    return url_list


###�python2.6  getOriAccount.py url_name_openid_0824
if __name__ == '__main__':
    if len(sys.argv) < 4:
        print >> sys.stderr, "ERROR...argv need 4 argvs"
        exit(1)
    main_judge_orignal(sys.argv[1],sys.argv[2],sys.argv[3])
