#!/usr/bin/python2.6
#-*-encoding:utf-8-*-

from liblinearutil import *
def test_liblinear():
    y, x = svm_read_problem('../heart_scale')
    m = train(y[:200], x[:200], '-w1 3 -c 5')
    #m = train(y[:200], x[:200], '-w1 3 -v 5')
    save_model("./test",m)
    p_lable, p_acc, p_val = predict(y[200:], x[200:], m) # use the qian 200 rows train the model and use this model to predict with hou 70 rows and p_lables is a list of predicted labels; p_acc is a tuple including accuracy(×¼È·ÂÊ),mean squared error, and squared correlation coefficient
    print "**********zyp********"
    print "labels_size=%d,features_size=%d" % (m.get_nr_class(),m.get_nr_feature())
    #print y
    #print "********"
    #print x # y is the lables of all the 270 rows and x is the datas of all the 270 rows
    print "%s ** %s ** %s" % (len(p_lable), len(p_acc), len(p_val))
    print "%s -- %s -- %s" % (p_lable, p_acc, p_val)

def read_liblinear():
	y, x = svm_read_problem('data.txt')
	m = load_model('model_file')
	save_model('model_file',m)

def self_data_liblinear():
    y, x = [4,1,-1,2,2,1,3,3],[{1:3.9,2:4.1,3:4.4},{1:1,3:1},{1:-1,3:-1},{1:2,3:2},{1:1.7,3:1.6},{1:1.3,2:1.5,3:1.4},{1:3.1,2:3.0,3:3.0},{1:2.8,3:2.9}] # the needed format dataset
    #prob = problem([1,-1],[{1:1,3:1},{1:-1,3:-1}])
    prob = problem(y, x)
    m = train(prob,'-c 4')
    #m = train(prob,'-v 4')
    save_model('model_file',m)
    #p_labels, p_acc, p_vals = 
    print "labels_size=%d,features_size=%d" % (m.get_nr_class(),m.get_nr_feature())

def cross_validata():
    y, x = [4,1,-1,2,2,1,3,3],[{1:3.9,2:4.1,3:4.4},{1:1,3:1},{1:-1,3:-1},{1:2,3:2},{1:1.7,3:1.6},{1:1.3,2:1.5,3:1.4},{1:3.1,2:3.0,3:3.0},{1:2.8,3:2.9}] # the needed format dataset
    prob = problem(y, x)
    m = train(prob,'-w1 3 -w-1 1 -v 4') # cross validation train just return the cross validation accuracy
    print m

if (__name__ == "__main__"):
    test_liblinear()
    print "**** the next problem:****"
    self_data_liblinear()
    #read_liblinear()
    cross_validata()
