#!usr/bin
#coding=gbk
#__author__ = "ouyuanbiao"

input="/logdata/uigs/appsearch/201506/2015062[2-8]/*.lzo"
output="ouyuanbiao/complete_output"

hadoop fs -rm -r -skipTrash $output
hadoop org.apache.hadoop.streaming.HadoopStreaming \
-input $input \
-output $output \
-file parse_app_event.py \
-file reduce_calculate_channel_event.py \
-mapper "python parse_app_event.py" \
-reducer "python reduce_calculate_channel_event.py" \
-inputformat com.hadoop.mapred.DeprecatedLzoTextInputFormat \
-numReduceTasks 100 \

