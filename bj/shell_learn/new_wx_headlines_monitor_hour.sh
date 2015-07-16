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
	start_time=`date -d "-1 hour" +"%Y-%m-%d %H:00:00"`
fi	

hour=$3
if [[ -z ${hour} ]];then
	hour=`date -d "-1 hour" +"%Y%m%d%H"`
fi	


echo `date +"%Y-%m-%d %H:%M"`$'\t'"start_time=${start_time}"
echo `date +"%Y-%m-%d %H:%M"`$'\t'"hour=${hour}"
inputfile=/search/wangxiangming/code/Weixin_report/output/${LOG_FLAG}/output_${LOG_FLAG}.${hour}
echo `date +"%Y-%m-%d %H:%M"`$'\t'"input is:${inputfile}"

echo `date +"%Y-%m-%d %H:%M"`$'\t'"wx_headlines_monitor..."
${PYTHON} new_wx_headlines_monitor.py "${start_time}" "2" "${LOG_FLAG}" "${inputfile}" 1>>${LOG}/std.wx_headlines_monitor_hour_${LOG_FLAG} 2>>${LOG}/err.wx_headlines_monitor_hour_${LOG_FLAG}

echo `date +"%Y-%m-%d %H:%M"`$'\t'"abtest_wx_headlines_monitor..."
${PYTHON} abtest_wx_headlines_monitor.py "${start_time}" "2" "${LOG_FLAG}" "${inputfile}" 1>>${LOG}/std.wx_headlines_monitor_hour_${LOG_FLAG}_abtest 2>>${LOG}/err.wx_headlines_monitor_hour_${LOG_FLAG}_abtest

