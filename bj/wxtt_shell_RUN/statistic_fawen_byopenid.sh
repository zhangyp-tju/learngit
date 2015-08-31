#!/bin/sh 
#coding=utf-8

#mv query_age_sex query_age_sex_sample
#mkdir query_age_sex

#mkdir ./input_arts/05_arts
#cp ./input_arts/201505* ./input_arts/05_arts
#mkdir ./input_arts/06_arts 
#cp ./input_arts/201506* ./input_arts/06_arts 
#mkdir ./input_arts/07_arts 
#cp ./input_arts/201507* ./input_arts/07_arts 
#
## sample you can do as it:
## mkdir mkdir ./input_arts/08_arts
## mv ./input_arts/201508* ./input_arts/08_arts
## python2.6 statistic_fawen_byopenid.py ./input_arts/08_arts/ 08_fawen_result 
## 对应的更改*._2.sh 即可
#
#python2.6 statistic_fawen_byopenid.py ./input_arts/05_arts/ 05_fawen_result
#python2.6 statistic_fawen_byopenid.py ./input_arts/06_arts/ 06_fawen_result
#python2.6 statistic_fawen_byopenid.py ./input_arts/07_arts/ 07_fawen_result 
#
python2.6 statistic_fawen_byopenid.py $1 $2 



