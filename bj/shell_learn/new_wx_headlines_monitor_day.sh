#!/usr/bin/bash
set -x
PYTHON="/usr/bin/python2.6"
LOG="../log"

LOG_FLAG=$1
if [[ -z ${LOG_FLAG} ]];then
	echo "Please give the flag: online1 or independ in the first argv"
	exit 1
fi
if [[ ${LOG_FLAG} != "online1" && ${LOG_FLAG} != "independ" ]];then
	echo "the flag is illegal! Please chose online1 or independ in the first argv"
	exit 1
fi

start_time=$2
if [[ -z ${start_time} ]];then
	start_time=`date -d "-1 day" +"%Y-%m-%d"`
fi	

day=$3
if [[ -z ${day} ]];then
	day=`date -d "-1 day" +"%Y%m%d"`
fi	


echo `date +"%Y-%m-%d %H:%M"`$'\t'"start_time=${start_time}"
echo `date +"%Y-%m-%d %H:%M"`$'\t'"day=${day}"
inputfile=/search/wangxiangming/code/Weixin_report/output/${LOG_FLAG}/output_${LOG_FLAG}.${day}
echo `date +"%Y-%m-%d %H:%M"`$'\t'"input is:${inputfile}"

echo `date +"%Y-%m-%d %H:%M"`$'\t'"new_wx_headlines_monitor..."
${PYTHON} new_wx_headlines_monitor.py "${start_time}" "1" "${LOG_FLAG}" "${inputfile}" 1>>${LOG}/std.wx_headlines_monitor_day_${LOG_FLAG} 2>>${LOG}/err.wx_headlines_monitor_day_${LOG_FLAG}
