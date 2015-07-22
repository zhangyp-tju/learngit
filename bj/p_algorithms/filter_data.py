#!/usr/bin/python2.6 
#-*-encoding:utf8-*-

def filter_eachline(infilepath):
    """give the file and ele_num needed to split"""
    ele_num = 1
    err_cnt = 0
    outfilepath = "%s_NEW" % infilepath
    fw = open(outfilepath,'w')
    with open(infilepath) as fr:
        for line in fr:
            line_new = line.strip()
            if not line_new or line_new.strip()=="":continue
            eles = line_new.split(" ",ele_num)
            try:
                print >>fw, "%s,%s" % (eles[0],eles[1].strip())
            except:
                err_cnt += 1
    print err_cnt
            #for ele in eles:
                #print ele.strip()


if (__name__ == "__main__"):
    """main"""
    infilepath = "./test.data"
    filter_eachline(infilepath)


