#!/bin/bash
#-*-coding:gbk

#下载类别体系以及对应的关键词和账号
mysql -h 10.134.78.228 -udarrenan -pdarrenan db_personalized_reading --default-character-set=gbk -e "select id,first_level_topic,\
	second_level_topic,third_level_topic,type,keyword_account,level,info from t_list_page" > t_list_page.tmp
awk 'NR<10{print $0}' t_list_page.tmp > t_list_page.txt
dos2unix t_list_page.txt
rm -f t_list_page.tmp


#mongo 10.134.44.83:27026/WeiXinRecom  -eval "db.weixin_articles.count();" > t_zyp.tmp
#mongo 10.134.44.83:27026/WeiXinRecom  -eval "db.weixin_articles.find().limit(10).forEach(printjson);" > t_zyp.tmp
mongo 10.134.44.83:27026/WeiXinRecom  -eval "db.weixin_articles.find({"status":0}).limit(2).forEach(printjson);" > t_zyp.tmp

awk 'NR>2{print $0}' t_zyp.tmp > t_zyp.txt
dos2unix t_zyp.txt
rm -f t_zyp.tmp
