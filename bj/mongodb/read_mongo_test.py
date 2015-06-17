#!/usr/bin/python
#-*-encoding:utf-8-*-

import hashlib
import pymongo
def main():
    SOURCE_IP = "10.136.20.106"
    SOURCE_PORT = 27070
    conn_src = pymongo.Connection(host=SOURCE_IP,port=SOURCE_PORT)
    db_src_article = conn_src.WeiXinRecom.weixin_articles
    res_arts = db_src_article.find({'keywords':{'$exists':True}},{'keywords':1}).limit(30)#pymongo is sensitive '',True not true
    
    cp = 0
    for art in res_arts:
        cp = cp + 1
        print "di:%d -- art:id = %s ;" %(cp,art.get('_id','10000').encode('gbk','ignore'))
        keywords = art.get('keywords',[])
        if not keywords:# empty
            print "keywords is an empty list[]..."
            continue
        for word in keywords:#keywords is collection of lists
            if not word:
                print "kong"
            for ele in word:
                if type(ele)==list:
                    for e in ele:
                        print "e = %s" %e
                else:#word,pos
                    print "ele = %s" % ele#.encode('gbk','ignore')
    # close
    conn_src.close()
    '''格式如下：
    { "_id" : "42c4a9be657885b3df63e47d4d41308f", "keywords" : [ ] }
    { "_id" : "689ef41d47a05c5159e06e04b4c0165e", "keywords" : [  [  "锟斤拷锟斤拷",  [  1,  "锟斤拷司锟斤拷锟斤拷" ] ],  [  "锟斤拷锟斤拷",  [  1,  "锟斤拷锟斤拷锟斤拷锟斤拷" ] ] ] }
    { "_id" : "76edf0b9b3c246eec6c1ab4b0e54e234", "keywords" : [  [  "装锟斤拷",  5 ],  [  "锟斤拷锟斤拷",  5 ],  [  "装锟斤拷",  5 ] ] }

    isinstance可以用来判断一个变量是否属于一个类。 在python里应该是正确的。
     if type(x)==list:pass
      if type(x)==dict:pass
    '''

def split_join():
    str1 = '1,2,3'
    str_list = str1.split(',',1)
    print str_list

    str_2 = '\t'.join(str_list)
    print str_2

if (__name__ == "__main__"):
    main()
    split_join()
