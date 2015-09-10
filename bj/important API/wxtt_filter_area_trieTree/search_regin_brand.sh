#!/bin/bash
#coding=utf-8

#### 根据日期选项生成输入文件
#START_DAY=20150701
#END_DAY=20150831
#OUTPUT_FILE_PRE="./filter_area.result" # 需要统计的openid文件
#### 根据需要更改起止日期
#
## date2seconds
#START_DAY_SECOND=`date -d "${START_DAY}" +%s`
#END_DAY_SECOND=`date -d "${END_DAY}" +%s`
#TODAY_SECOND=`date +%s`
#DAY_SECOND=`expr 24 \* 60 \* 60`
#
#START_S=`expr $TODAY_SECOND - $START_DAY_SECOND`
#END_S=`expr $TODAY_SECOND - $END_DAY_SECOND`
#
#START=`expr $START_S / $DAY_SECOND`
#END=`expr $END_S / $DAY_SECOND`
#
#inputdir=../historyData/ # 输入文件
#tmpfile=${START_DAY}_${END_DAY}
#
####准备数据
#if [ -f $tmpfile ]
#then
#        rm -f $tmpfile
#fi
#printf "****$START,$END\n"
#for((i=$START;i>=$END;i--))
#do
#        filename=`date -d "-$i days" +%Y%m%d`
#        echo $filename
#        if [ -f $inputdir/$filename ]
#        then
#                cat $inputdir/$filename >> $tmpfile
#                #cp $inputdir/$filename  $tmpdir
#        fi  
#done
##
#
#
##### 功能一 ---- 识别出区域（地域） 和 自宣传账号
#now_time=`date "+%Y%m%d %H:%M:%S"`
#printf "START filter_area... [ ${now_time} ]...\n"
#cat ${tmpfile} | python2.6 search_regin_brand.py 1> ${OUTPUT_FILE_PRE}${tmpfile}
#now_time=`date "+%Y%m%d %H:%M:%S"`
#printf "END filter_area... [ ${now_time} ]...\n"


#### 功能一 ---- 识别出区域（地域） 和 自宣传账号
now_time=`date "+%Y%m%d %H:%M:%S"`
printf "START filter_area... [ ${now_time} ]...\n"
cat ./tmp.data | python2.6 search_regin_brand.py 1> tmp.result
now_time=`date "+%Y%m%d %H:%M:%S"`
printf "END filter_area... [ ${now_time} ]...\n"
