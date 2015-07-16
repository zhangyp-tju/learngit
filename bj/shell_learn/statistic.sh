#!/bin/sh
#-*-encoding:utf8-*-

# Author: zyp
# Written: Jun 13, 2015
# Modified: Jun 13,2015
# Purpos: To establish the statistic data about subtopc_1 by 5 level from 10.144.85.109:17016 WeiXinRecom.weixin_articles
#Brief Description: WeiXinRecom (just the latest ten days data with the file  account_weight.mysql statistic0706.py and matching)
'''
crontab -e
crontab -l
#yapeng subtopic_data_5
#*/30 * * * * cd /search/yapeng/subtopic_data; sh test.sh >> ./logs/subtopic_data_5.log 2>&1
15 12 * * * cd /search/yapeng/subtopic_data; sh statistic.sh >> ./logs/subtopic_data_5.log 2>&1
'''
PYTHON='/usr/bin/python2.6'

T_DATE=$(date +%Y%m%d)
Y_DATE=$(date -d last-day +%Y%m%d)
TIME=`date "+%Y-%m-%d %H:%M:%S"`
printf "\n\n***********BEGIN(${TIME})*************\n"
printf "today: ${T_DATE} and yestoday: ${Y_DATE}\n"
filename="statistic.csv"

new_filename=${filename}"$Y_DATE" # strs combine together
#printf "${new_filename}"

#mv ./${filename} ./${new_filename}

if test ! -f "$filename";then
    printf "this file (${filename}) not exists or not a regular file.\n"
    #exit 1
else #:
    mv ./${filename} ./${new_filename}
    printf "move file ${filename} to ${new_filename} Successfully...\n"
fi

# call for statistic commands file 
cmd_file="d_statistic_garry_finall.py"
#python2.6 ./${cmd_file}
${PYTHON} ./${cmd_file}
TIME=`date "+%Y-%m-%d %H:%M:%S"`
printf "create or rewrite the file statistic.csv Successfully...(Change 20150714 add CTR)\n"
printf "***************END(${TIME})******************\n\n"
