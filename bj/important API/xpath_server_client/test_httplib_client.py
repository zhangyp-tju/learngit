#!/usr/bin/python2.6
#coding=gbk
__author__ = "yitian"

import sys
import json
import urllib
import urllib2
url = "http://192.168.175.128:8899" # this ip is from ifconfig cmd and the host can reach this url...
data = {}
data["mids"] = []

def get_post_res(data):
    data = urllib.urlencode(data)
    req = urllib2.Request(url, data)
    #req.add_header('Content-Type', 'application/json; charset=utf-8')
    resp = urllib2.urlopen(req)
    result = resp.read()# 三步实现req访问，urllib.urlencode(data),urllib2.Request(url,data),urllib2.urlopen(req)
    user_infos = json.loads(result, encoding="gbk").get("result") # 返回的是json字符串，json.loads()之后，是list还是dict就比较任意的取了
    return user_infos

def main():
    data["mids"] = ['zyp','all']
    user_infos = get_post_res(data)
    print "###",user_infos
    #print json.dumps(user_infos, ensure_ascii=False).encode("gbk")
    try:
        name = user_infos.get(u"姓名","") # 实现了 key value的中文传递
        sex = user_infos.get("sex","")
        age = user_infos.get("age",-1)
    except:
        print "ERROR: msg...."
    print "%s\t%s\t%s\n" % (name,age,sex)
    #print "mid:%s sex:%s age1:%s age2:%s" % (mid.encode("gbk"), sex.encode("gbk"), age1, age2)


if __name__ == "__main__":
    print "..."
    main()



