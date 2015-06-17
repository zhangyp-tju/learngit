import hashlib
import pymongo
def main():
    #DEST_IP = "10.136.20.106"
    DEST_IP = "10.134.44.83"
    #DEST_PORT = 27070
    DEST_PORT = 27026
    conn_dest = pymongo.Connection(host=DEST_IP,port=DEST_PORT)
    db_dest_article = conn_dest.WeiXinSubtopicPlatform.weixin_articles
    with open('jiaozheng_subtopic.dat') as f:
        count = 0
        for line in f:
            count += 1
            tups = line.strip('\n').split('\t')
            if len(tups) != 7:continue
            art = {}
            art['topic1'] = tups[0]
            subtopic_1 = tups[1]
            if subtopic_1 == "NULL":subtopic_1 = ""
            art['subtopic_1'] = subtopic_1
            art['title'] = tups[2]
            art['summary'] = tups[3]
            art['account'] = tups[4]
            art['account_openid'] = tups[5]
            art['url'] = tups[6]
            art['signature'] = -1

            art['_id'] = hashlib.md5(art['url']).hexdigest()
            art['op_time'] = 1433088000
            art['read_num'] = -1
            art['base_rank'] = -1 
            art['review'] = 1
            art['page_time'] = 1433088000 
            db_dest_article.save(art)
        print count


main()
