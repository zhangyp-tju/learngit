#!/usr/bin/python
#-*-encoding:utf-8-*-

import hashlib
import pymongo
def main():
    SOURCE_IP = "10.136.20.106"
    #DEST_IP = "10.134.44.83"
    SOURCE_PORT = 27070
    #DEST_PORT = 27026
    conn_src = pymongo.Connection(host=SOURCE_IP,port=SOURCE_PORT)
    db_src_article = conn_src.WeiXinRecom.weixin_articles
    '''
    res_arts = db_src_article.find({'keywords':{'$exists':True}},{'keywords':1}).count()
    print "****"
    print res_arts
    '''
    res_arts = db_src_article.find({'keywords':{'$exists':True}},{'keywords':1}).limit(30)
    
    # db.weixin_articles.find({keywords:{$exists:true}},{keywords:1})
    cp = 0
    # test list
    li = [ ]
    if li:
        print "not kong"
    else:
        print "kong kong"
    print "len(li) = %d" % len(li)
    # end test
    for art in res_arts:
        cp = cp + 1
        print "di:%d -- art:id = %s ;" %(cp,art.get('_id','10000').encode('gbk','ignore'))
        keywords = art.get('keywords',[])
        if not keywords:
            print "keywords is an empty list[]"
            continue
        for word in keywords:
            #if len(word) == 0:
            if not word:
                print "kong"
            #print word # 整体输出就是  ['\xca\xae\xb6\xfe\xd0\xc7\xd7\xf9', 5]  ,,十二星座   ,,5  --- list
            for ele in word:
                if type(ele)==list:
                    for e in ele:
                        print "e = %s" %e
                else:
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
if (__name__ == "__main__"):
    main()
