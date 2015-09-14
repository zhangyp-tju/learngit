#!/usr/bin/python 
#coding=utf-8

import hashlib
import pymongo
import sys

#DEST_IP = "10.136.20.106"
DEST_IP = "127.0.0.1"
#DEST_IP = "10.134.44.83"
#DEST_PORT = 27070
DEST_PORT = 27017
#DEST_PORT = 27026

def get_conn():
    #return pymongo.Connection(host=DEST_IP,port=DEST_PORT)
    return pymongo.MongoClient(host=DEST_IP,port=DEST_PORT)

def get_cursor(conn):
    condictions = {"account_openid":1,"account":1,"topic1":1,"subtopic_1":1,"read_num":1,"title":1,\
    "title_seg":1,"url":1,"page_time":1,"review":1}
    db_src = conn.tju_cn.weixin_articles
    return db_src.find({},condictions).limit(20) # or db = conn[db_name][coll_name]

def export_to_file():
    conn_src = get_conn()
    cur_src = get_cursor(conn_src)
    with open("./pymongo.data2",'w') as fpw:
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
            
            line.append(art.get("account_openid").encode("gbk")) # 0
            line.append(art.get("account").encode("gbk")) #１
            line.append(art.get("url").encode("gbk")) # 2
            line.append(art.get("title").encode("gbk")) # 3
            line.append(art.get("topic1","").encode("gbk"))
            line.append(art.get("subtopic_1","").encode("gbk")) # 5
            line.append(str(art.get("page_time").encode("gbk")))
            line.append(art.get("title_seg","").encode("gbk")) # 7
            line.append(art.get("_id").encode("gbk"))
            line.append(str(art.get("review",-1).encode("gbk"))) # 9
            line.append(str(art.get("read_num",-1).encode("gbk")))
            print >> sys.stderr, line[1],line
            print "\t".join(line)
            #fpw.write("\t".join(line) +"\n")
        # end for
        #print count
    # end with
    conn_src.close()



def import_from_file():
    conn_dest = get_conn()
    db_dest = conn_dest.tju_cn.test # or db = conn[db_name][coll_name]
    arts = []
    with open('pymongo.data2') as fpr:
        count = 0
        for line in fpr:
            count += 1
            tups = line.strip('\n').split('\t')
            if len(tups) != 11:continue
            #art = {}
            #art['account_openid'] = tups[0]
            #art['account'] = tups[1]
            #art['url'] = tups[2]
            #art['title'] = tups[3]
            #art['topic1'] = tups[4]
            #art['subtopic_1'] = tups[5]
            #art['page_time'] = tups[6]
            #art['tile_seg'] = tups[7]
            #art['_id'] = tups[8]
            ##art['_id'] = hashlib.md5(art['url']).hexdigest()
            #art['review'] = tups[9]
            #art['read_num'] = tups[10]

            art = {}
            art['account_openid'] = tups[0]#.decode("utf-8")
            art['account'] = tups[1].decode("gbk")
            art['url'] = tups[2]
            art['title'] = tups[3].decode("gbk")
            art['topic1'] = tups[4].decode("gbk")
            art['subtopic_1'] = tups[5].decode("gbk")
            art['page_time'] = tups[6]
            art['tile_seg'] = tups[7].decode("gbk")
            art['_id'] = tups[8]
            #art['_id'] = hashlib.md5(art['url']).hexdigest()
            art['review'] = tups[9]
            art['read_num'] = tups[10]

            #db_dest.save(art) ### 改为批量插入数据库
            arts.append(art)
        # end for
        print >> sys.stderr, count
    # end with

    db_dest.insert(arts)
    conn_dest.close()
### python2.6 restore_reviewed_data.python
### python2.6 restore_reviewed_data.python > pymongo.data2

####
'''
mongo 库是utf-8格式的，但是控制台目前仅仅能够输出utf-8格式的unicode格式，gbk格式的乱码；
而输出到文件恰恰相反，gbk格式的文件可以正确输出，utf-8格式的无法输出到文件中；这也是为什么从数据库里面查询出来的art,
控制台可以直接打印，非常完好。但是要想输出到文件中，每一个字段都需要encode("gbk")
从文件导入到数据库：
文件中编码应该是gbk,而库里面是utf-8，因此要decode("gbk") 为unicode
'''
#### 可以直接在这里创建数据库名称，而不用事先创建；链接即创建;集合也是一样

if __name__ == "__main__":
    #export_to_file()
    import_from_file()
