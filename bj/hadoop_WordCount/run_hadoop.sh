#!usr/bin
#coding=gbk
#__author__ = "ouyuanbiao"

input="denghailong/app_search/log/201506/part-*"
output="ouyuanbiao/anit_spam_output"

hadoop fs -rm -r -skipTrash $output
hadoop org.apache.hadoop.streaming.HadoopStreaming \
-input $input \
-output $output \
-mapper "python ./mapper.py" \
-file ./mapper.py \
-file reduce_calculate_channel_event.py \
-reducer "python reduce_calculate_channel_event.py" \
-numReduceTasks 100 \

