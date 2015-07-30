#!/usr/bin/python2.6 
#coding=gbk

import sys
import load_attr_list

def filter_tag_attribute():
    ''''''
    attr = load_attr_list.get_attr_list()
    spliting_file_path = 'tag_account.cnt.final.deleteDigit.seg_new'
    regex = '\t'
    fp = open(spliting_file_path,'w')
    for line in sys.stdin:
        line = line.strip()
        if not line: continue
        try:
            words = line.split(regex,3)
        except:
            print >> sys.stderr,"ERROR split ...%s " % (line)
        if len(words) != 4:
            print >> sys.stderr, "ERROR words ...."
        try:
            fp.write(words[0] + "\t" + words[1] + "\t" +words[2] + "\t" + attr[int(words[3])])
        except:
            print >> sys.stderr, "ERROR in int %s" % (words[3])
    
    print "END..."

# only change to attr
'''
if __name__ == "__main__":
    ''''''
    attr = load_attr_list.get_attr_list()
    spliting_file_path = 'tag_account.cnt.final.deleteDigit.seg_new'
    regex = '\t'
    fp = open(spliting_file_path,'w')
    for line in sys.stdin:
        line = line.strip()
        if not line: continue
        try:
            words = line.split(regex,3)
        except:
            print >> sys.stderr,"ERROR split ...%s " % (line)
        if len(words) != 4:
            print >> sys.stderr, "ERROR words ...."
        w_nums = words[3].strip().split(' ')
        new_line = words[0] + "\t" + words[1] + "\t" +words[2] + "\t"
        if len(w_nums)==1: 
            try:
                new_line +=  attr[int(w_nums[0])]
            except:
                print >> sys.stderr, "ERROR in int %s" % (words[3])
        else:
            try:
                for w_num in w_nums:
                    new_line += (attr[int(w_num)] + ' ')
            except:
                print >> sys.stderr, "ERROR in int %s" % (words[3])
        fp.write(new_line.strip() + "\n")
    
    print "END..."
 '''

if __name__ == "__main__":
    ''' run this conmand like this: cat tag_account.cnt.final.deleteDigit.seg | python2.6 change_digs2attr.py'''
    cnt = 0
    attr = load_attr_list.get_attr_list()
    pre_file_path = './split_arr/tag_account_new_'
    regex = '\t'
    fp = open('./split_arr/tag_spliting','a')
    for line in sys.stdin:
        line = line.strip()
        if not line: continue
        try:
            words = line.split(regex,3)
        except:
            print >> sys.stderr,"ERROR split ...%s " % (line)
        if len(words) != 4:
            print >> sys.stderr, "ERROR words ...."
        w_nums = words[3].strip().split(' ')
        new_line = words[0] + "\t" + words[1] + "\t" +words[2] + "\t"
        if len(w_nums)==1: 
            try:
                new_line +=  attr[int(w_nums[0])]
            except:
                print >> sys.stderr, "ERROR in int %s" % (words[3])
            '''
            if int(w_nums[0]) in del_attr:
                cnt += 1
                print "%s" % (new_line)
                continue
            '''
            del_fp = open((pre_file_path + w_nums[0]).strip(),'a')
            del_fp.write(new_line + '\n')
            del_fp.close()
            continue
        else:
            try:
                for w_num in w_nums:
                    new_line += (attr[int(w_num)] + ' ')
            except:
                print >> sys.stderr, "ERROR in int %s" % (words[3])
        fp.write(new_line.strip() + "\n")
    fp.close()
    print >> sys.stderr, "the del lines is %d" % (cnt)
    print "END..."

