#!/bin/bash 
#coding=utf-8

CMD="python2.6 manage.py runserver 0.0.0.0:8889"
LOGS='./log'
#T_DATE=$(date + "%Y-%m-%d %H:%M:%S")
T_DATE=`date "+%Y-%m-%d %H:%M:%S"`
exec 8>&1
exec 1>>${LOGS}

printf "\n\n ********************************BEGIN*************************************\n"

# running pro in backgroud and output redirect to ./log and test firstly
lists=`ps aux | grep manage.py | grep runserver | grep 0.0.0.0:8889`
PID_INDEX=2
LINE_LEN=14
cnt=0
for cmd in ${lists}
do
    cnt=`expr ${cnt} + 1`
    if test `expr ${cnt} % ${LINE_LEN}` -eq ${PID_INDEX}
    then
        printf "The server is RUNNING,the manage.py runserver on 0.0.0.0:8889 of pid (${cmd}) will be killed first and Restart it \n"
        kill -9 ${cmd}
    fi
done

printf "Restart the server(manage.py runserver 0.0.0.0:8889) at time: ${T_DATE}\n"
nohup ${CMD} 1>>${LOGS} 2>&1 &

print "\n ****running ....\n"

exec 1>&8 8>&-
# monitor the tail of logfile
if test ! -f "${LOGS}";then
    printf "the file(${LOGS} is not exists or not a normal file)"
else
    tail -f log
fi
