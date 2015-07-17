#!usr/bin
#coding=gbk
#__author__ = "test"

# the first MR
input="yapeng/join/input/*"
output="yapeng/join/output"

hadoop fs -rm -r -skipTrash $output
hadoop org.apache.hadoop.streaming.HadoopStreaming \
-input $input \
-output $output \
-mapper "python join_mapper.py"  -file ./join_mapper.py \
-reducer "python join_reducer.py"  -file ./join_reducer.py \
-numReduceTasks 2 \

# the second MR
input="yapeng/join/output/*"
output="yapeng/join/result"

hadoop fs -rm -r -skipTrash $output
hadoop org.apache.hadoop.streaming.HadoopStreaming \
-input $input \
-output $output \
-mapper "python join_mapper2.py"  -file ./join_mapper2.py \
-reducer "python join_reducer2.py"  -file ./join_reducer2.py \
-numReduceTasks 1 \



