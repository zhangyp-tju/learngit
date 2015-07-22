#!/usr/bin/python2.6 
#-*-encoding:utf-8-*-
import kNN
import numpy as np

dataSet, labels = kNN.createDataSet()

testX = np.array([1.2, 1.0])
k = 3
outputLabel = kNN.kNNClassify(testX, dataSet, labels, 3)
print "Your input is:", testX, "and classified to class: ", outputLabel

testX = np.array([0.1, 0.3])
outputLabel = kNN.kNNClassify(testX, dataSet, labels, 3)
print "Your input is:", testX, "and classified to class: ", outputLabel

testX = np.array([1.2,0.3])
outputLabel = kNN.kNNClassify(testX, dataSet, labels, 3)
print "Your input is:", testX, "and classified to class: ", outputLabel



