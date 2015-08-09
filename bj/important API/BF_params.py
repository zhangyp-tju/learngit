#!/usr/bin/python2.6 
#coding=gbk

import math

fp = 0.01
#Num_key = 10760000 # garry 109
Num_key = 80000  # garry 109


def get_params_BT():
    global fp,Num_key
    #print math.e,math.log(10,math.e)
    k = -math.log(fp,math.e) // math.log(2,math.e)
    m = math.log(fp,math.e) *Num_key / math.log(0.6185,math.e)
    f = (1 - math.e ** (-k*Num_key/m)) ** k
    return k,f,m

if __name__ == "__main__":
    
    kNum_hash,fp_new,mLen_bit = get_params_BT()
    print "kNum_hash=%s,fp_new=%s,mLen_bit=%s" % (kNum_hash,fp_new,mLen_bit)
