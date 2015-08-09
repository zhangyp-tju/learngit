#!/usr/bin/python2.6 
#coding=utf-8

import urllib2

def login_url(url):
    google = urllib2.urlopen(url)
    print 'http header:\n', google.info()
    print 'http status:', google.getcode()
    print 'url:', google.geturl()
    for line in google: # 就像在操作本地文件
        line = line.decode('utf-8').encode('gbk')
        print line,
    google.close()

if __name__ == "__main__":
    #url = "http://10.134.37.32/cweb/"
    #url = "http://10.134.37.33:8889/load_arts"
    url = "http://blog.csdn.net/u010700335/article/details/41170645" # can not get the content otherwise the baidu and google
    login_url(url) 
