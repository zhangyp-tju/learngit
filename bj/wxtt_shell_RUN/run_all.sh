#!/bin/bash
#coding=utf-8

# 根据日期选项生成输入文件
START_DAY=20150821
END_DAY=20150822
OPENID_FILE="./openid" # 需要统计的openid文件
### 根据需要更改起止日期

TODAY=`date "+%Y%m%d"`
inputdir=./historyData/ # 输入文件
outputdir=./out_results/${START_DAY}_${END_DAY} # 结果输出文件
mkdir ${outputdir}
tmpfile=./input_tmp/${START_DAY}_${END_DAY}
tmpdir=${tmpfile}"_dir"
printf "${tmpdir}\n"
mkdir ${tmpdir}
###准备数据
if [ -f $tmpfile ]
then
        rm -f $tmpfile
fi
END=`expr $TODAY - $START_DAY`
START=`expr $TODAY - $END_DAY`
#printf "$START,$END\n"
for((i=$START;i<=$END;i++))
do
        filename=`date -d "-$i days" +%Y%m%d`
        echo $filename
        if [ -f $inputdir/$filename ]
        then
                cat $inputdir/$filename >> $tmpfile
                cp $inputdir/$filename  $tmpdir
        fi  
done

### 功能五 ----- 原创 data from tmpfile and given openid; and outpath is ${tmpfile}"_ori"
now_time=`date "+%Y%m%d %H:%M:%S"`
printf "END INITIAL [ ${now_time} ]...\n"
sh ./getOriAccount.sh ${OPENID_FILE} ${tmpfile}
now_time=`date "+%Y%m%d %H:%M:%S"`
printf "END getOriAccount.sh [ ${now_time} ]...\n"

### 功能五 -2 ------ 统计原始文章数目 data from ${tmpfile}"_ori"
sh ./getOriAccount_2.sh ${tmpfile}"_ori" ${outputdir}/getOriAccount_2.csv

### 功能三 ----- 被转载率/被转载文章数/被转载次数 data from mongodb no time or date limit no filter by openid
des=${outputdir}/get_reprint_rate_arts.csv
#now_time=`date "+%Y%m%d %H:%M:%S"`
#printf "END INITIAL [ ${now_time} ]...\n"
sh ./get_reprint_rate_arts.sh ${OPENID_FILE} ${des}
now_time=`date "+%Y%m%d %H:%M:%S"`
printf "END reprint [ ${now_time} ]...\n"

### 功能一 ---- 发文频率和篇数 data from myin ${tmpdir}
now_time=`date "+%Y%m%d %H:%M:%S"`
printf "S fawen [ ${now_time} ]...\n"
des_tmp=${outputdir}/statistic_fawen_byopenid.csv
# ori des two path as followings
sh ./statistic_fawen_byopenid.sh ${tmpdir} ${des_tmp}
sh ./statistic_fawen_byopenid_2.sh ${des_tmp} ${des_tmp}_2
sh ./statistic_fawen_byopenid_3.sh ${des_tmp}_2 ${des_tmp}_3
now_time=`date "+%Y%m%d %H:%M:%S"`
printf "END fawen [ ${now_time} ]...\n"

#### 功能二 ----- 粉丝数 data from mongodb gary
des_tmp=./input_tmp/yuedu_fensi_bi_data
end=`date "+%Y%m%d"`
st=`date -d "-7 days" +%Y%m%d`
sh ./read_num_yuedu_fensi_bi_load_data.sh ${OPENID_FILE} ${des_tmp} ${st} ${end}
now_time=`date "+%Y%m%d %H:%M:%S"`
printf "END load_data from mongo_garry fensi [ ${now_time} ]...\n"
sh ./read_num_yuedu_fensi_bi_statistic.sh ${des_tmp} ${outputdir}/read_num_yuedu_fensi_bi_statistic.csv
now_time=`date "+%Y%m%d %H:%M:%S"`
printf "END statistic fensi [ ${now_time} ]...\n"



## 功能四 ----- 账号平均阅读数 data from ${tmpfile}
#now_time=`date "+%Y%m%d %H:%M:%S"`
#printf "START avg_read [ ${now_time} ]...\n"
des=${outputdir}/updateAverageReadnum.csv
sh ./updateAverageReadnum.sh ${tmpfile} ${des}
now_time=`date "+%Y%m%d %H:%M:%S"`
printf "END avg_read [ ${now_time} ]...\n"
