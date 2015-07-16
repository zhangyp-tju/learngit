#!usr/bin
#coding=gbk
#__author__ = "test"

input="yapeng/WC/input/*.txt"
output="yapeng/WC/output"

hadoop fs -rm -r -skipTrash $output
hadoop org.apache.hadoop.streaming.HadoopStreaming \
-input $input \
-output $output \
-mapper "python word_count_mapper.py"  -file ./word_count_mapper.py \
-reducer "python word_count_ruducer.py"  -file ./word_count_ruducer.py \
-numReduceTasks 3 \

