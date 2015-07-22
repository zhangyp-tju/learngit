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

## step 1: load data
print "step 1: load data..."
dataSet = []
fileIn = open('./kmeans_dataset')
err = 0
for line in fileIn.readlines():
    lineArr = line.strip().split(',')
    try:
        dataSet.append([float(lineArr[0]), float(lineArr[1])])
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
k = 4
centroids, clusterAssment = kMeans.kmeans(dataSet, k)
print centroids # ÖÐÐÄ
print "*****"
print clusterAssment # lable and juli

## step 3: show the result
print "step 3: show the result..."
#showCluster(dataSet, k, centroids, clusterAssment)
