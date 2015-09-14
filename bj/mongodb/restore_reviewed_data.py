#!/usr/bin/python 
#coding=gbk

import hashlib
import pymongo

DEST_IP = "10.136.20.106"
#DEST_IP = "10.134.44.83"
DEST_PORT = 27070
#DEST_PORT = 27026

def get_conn():
    return pymongo.Connection(host=DEST_IP,port=DEST_PORT)

def get_cursor(conn):
    condictions = {"account_openid":1,"account":1,"topic1":1,"subtopic_1":1,"read_num":1,"title":1,\
    "title_seg":1,"url":1,"page_time":1,"review":1}
    db_src = conn.WeiXinSubtopicPlatform.weixin_articles
    return db_src.find({},condictions).limit(2000) # or db = conn[db_name][coll_name]

def export_to_file():
   #conn_src = get_conn()
    cur_src = get_cursor(conn_src)
    with open("./pymongo.data",'w') as fpw:
        # line = [] # wrong ERROR
        for art in cur_src:
            #print "dddd",art
            line = []
           # line.append(art.get("account_openid"))
           # line.append(art.get("account").decode("gbk"))
           # line.append(art.get("url"))
           # line.append(art.get("title").decode("gbk"))
           # line.append(art.get("topic1","").decode("gbk"))
           # line.append(art.get("subtopic_1","").decode("gbk"))
           # line.append(str(art.get("page_time")))
           # line.append(art.get("title_seg","").decode("gbk"))
           # line.append(str(art.get("review",-1)))
           # line.append(str(art.get("read_num",-1)))

            line.append(art.get("account_openid")) # 0
            line.append(art.get("account")) #１
            line.append(art.get("url")) # 2
            line.append(art.get("title")) # 3
            line.append(art.get("topic1",""))
            line.append(art.get("subtopic_1","")) # 5
            line.append(str(art.get("page_time")))
            line.append(art.get("title_seg","")) # 7
            line.append(art.get("_id"))
            line.append(str(art.get("review",-1))) # 9
            line.append(str(art.get("read_num",-1)))

            fpw.write("\t".join(line) +"\n")
        # end for
        #print count
    # end with
    conn_src.close()



def import_from_file():
    conn_dest = get_conn()
    db_dest = conn_dest.test.weixin_articles # or db = conn[db_name][coll_name]
    with open('pymongo.data') as fpr:
        count = 0
        for line in fpr:
            count += 1
            tups = line.strip('\n').split('\t')
            if len(tups) != 11:continue
            art = {}
            art['account_openid'] = tups[0]
            art['account'] = tups[1]
            art['url'] = tups[2]
            art['title'] = tups[3]
            art['topic1'] = tups[4]
            art['subtopic_1'] = tups[5]
            art['page_time'] = tups[6]
            art['tile_seg'] = tups[7]
            art['_id'] = tups[8]
            #art['_id'] = hashlib.md5(art['url']).hexdigest()
            art['review'] = tups[9]
            art['read_num'] = tups[10]

            db_dest.save(art)
        # end for
        #print count
    # end with
    conn_dest.close()
    
### python2.6 restore_reviewed_data.python

if __name__ == "__main__":
    #export_to_file()
    import_from_file()
