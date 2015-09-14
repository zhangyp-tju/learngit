#coding=gbk
#################################################
# kmeans: k-means cluster
# Author : zouxy
# Date   : 2013-12-25
# HomePage : http://blog.csdn.net/zouxy09
# Email  : zouxy09@qq.com
#################################################

import kMeans
from numpy import *
import time
#import matplotlib.pyplot as plt

#### 根据需要更改这里的
k = 5 
#dataset_file = './kmeans_dataset'
dataset_file = './kmeans_dataset_double'

####
## step 1: load data
print "step 1: load data..."
dataSet = []
fileIn = open(dataset_file)
err = 0
flag = 1
for line in fileIn.readlines():
    lineArr = line.strip().split(',')
    cols = []
    if flag:
        flag = 0
        cols_cnt = len(lineArr)
    for idx in range(cols_cnt): # 请事前清洗数据，把列数统一
        cols.append(float(lineArr[idx]))
    try:
        #dataSet.append([float(lineArr[0]), float(lineArr[1]),float(lineArr[2]), float(lineArr[3])]) ### change this line for cols
        dataSet.append(cols)
    except:
        print lineArr[0]
        err += 1
        pass
    finally:
        pass
        #print lineArr[0],lineArr[1]
print "err num= ", err
## step 2: clustering...
print "step 2: clustering..."
dataSet = mat(dataSet)
#k = 4
centroids, clusterAssment = kMeans.kmeans(dataSet, k)
print centroids # 中心
print "*****"
print clusterAssment # lable and juli

## step 3: show the result
print "step 3: show the result..."
#showCluster(dataSet, k, centroids, clusterAssment)
