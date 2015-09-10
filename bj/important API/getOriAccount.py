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

timeValue = time.strftime('%Y-%m-%d',time.localtime(time.time()))
LOG_FILE = 'log/' + timeValue
#TOPN = 100
ProcessNum = 5

openid_set = set() # for load_openid()

def isOriginal(url,openid):
    req_header = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 SE 2.X MetaSr 1.0',
                    #'Accept-Encoding':'gzip,deflate,sdch',
                    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    #'Cookie':'__v3_c_review_10170=0; __v3_c_last_10170=1412911510785; __v3_c_visitor=1412911510785668; 3g_guest_id=-9167205929542721536; qq_slist_autoplay=on; ts_uid=4404360900; _ga=GA1.2.131689453.1432083798; o_cookie=525607249; ptcz=71fed3a30143224b32a4228655d3bc9ded9ea682b9563abbb173c62117ec83f0; pt2gguin=o0525607249; uin=o0525607249; skey=@bGUN4EhF0; qm_username=525607249; qm_sid=fd0e4a54ab0f65a116421c437c028010,qcFU5UHA4S3N5eFdkSmd4Y1YxclZGT3RYZE5RbGRZcUU1Z05zTzFITFJsMF8.; ptisp=ctc; pgv_info=ssid=s5151319040; pgv_pvid=6656621400',
                    #'Accept-Language':'zh-CN,zh;q=0.8',
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
        lock.acquire()
        idx = idxArray[0]
        if idx % 100000 == 0:
            logging.info('crawl lines : %d' % idx)

        if (idx >= idxArray[1]):
            lock.release()
            break
        idxArray[0] = idx + 1
        lock.release()
        url_openid = requestArray[idx]
        cols = url_openid.split('\t')
        try:
            url = cols[0]
            openid_u_name = cols[-3]
            id_name = openid_u_name.split("##")
            #u_name = id_name[0]
            openid = id_name[1]
        except:
            print >> sys.stderr,"ERROR"
            continue

        ret = isOriginal(url,openid)
        #if  '该内容已被发布者删除' in html.decode('utf8','ignore').encode('gbk','ignore'):
        lock.acquire()
        #logging.info('%s\t1' % url_openid)
        #invalidUrl.append(url)
        print url_openid + '\t' + str(ret)
        sys.stdout.flush()
        lock.release()
# add by zyp
def load_openid(openid_file):
    with open(openid_file) as fpr:
        for line in fpr:
            line = line.strip()
            if not line:continue
            openid_set.add(line)

# generate one ulrs_list change by zyp
def getUrls(openid_file,tmpfile):
    load_openid(openid_file)
    url_list = []
    cnt = 0
    for line in open(tmpfile):
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
        if openid not in openid_set:
            continue
        url_list.append(line)
    return url_list

#http://mp.weixin.qq.com/s?__biz=MzA3ODc5MDEwNA==&mid=211215188&idx=1&sn=8f11f5930c0ae90eb265c7e25624c699&3rd=MzA3MDU4NTYzMw==&scene=6#rd  教你化妆与瘦身  oIWsFt4Qq2xa3B8Z65MuHFLPLFPA
#　python2.6  getOriAccount.py url_name_openid_0824
if __name__ == '__main__':
    begin_time = datetime.now()
    logging.basicConfig(level=logging.DEBUG,format='%(process)d %(asctime)s  %(levelname)s %(message)s',datefmt='%a, %d %b %Y',filename= LOG_FILE,filemode='w')
    processQueue = []
    #invalidUrl = []
    mgr = multiprocessing.Manager()
    idxArray = mgr.list()
    #invalidUrl = mgr.list()
    lock = multiprocessing.Lock()
    idxArray.append(0)
    tmpQueryArray = getUrls(sys.argv[1],sys.argv[2]) # call fetURLs fun
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
    #logging.info('%d invalid urls' % len(invalidUrl))
    #insert(invalidUrl)
    #update(invalidUrl)
    #writeIntoMysql(invalidUrl)
    end_time = datetime.now()
    logging.info('the cost time is %d s' % ((end_time-begin_time).seconds+0.0) )


