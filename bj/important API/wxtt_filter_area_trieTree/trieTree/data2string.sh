#!/bin/sh
#coding=gbk

set -x

num="eeee"
num2=${num}_ori
num3=${num2}".csv"
printf "ddd-- ${num} dd-- ${num2}",${num3}

st=`date "+%Y%m%d"`
end=`date -d "-7 days" +%Y%m%d`
printf "\n${st},,,${end}\n"


###
START_DAY=20150801
END_DAY=20150831
###

START_DAY_SECOND=`date -d "${START_DAY}" +%s`
END_DAY_SECOND=`date -d "${END_DAY}" +%s`
TODAY_SECOND=`date +%s`
DAY_SECOND=`expr 24 \* 60 \* 60`
printf "${START_DAY_SECOND},${END_DAY_SECOND},$TODAY_SECOND \n"

START_S=`expr $TODAY_SECOND - $START_DAY_SECOND`
END_S=`expr $TODAY_SECOND - $END_DAY_SECOND`

START=`expr $START_S / $DAY_SECOND`
END=`expr $END_S / $DAY_SECOND`

((sum=$START+$END))
sum2=$[$START+$END]
for((i=$START;i>=$END;i--))
do
    printf $i,"\t"
done

time printf '\n'$sum,$sum2'\n'
#但是对于批处理程序，一个处理流程，仅仅time了，但是你并不知道开始和结束时间；不过，他可以查看cup执行时间和i/o执行时间
printf "$START,$END \n"
