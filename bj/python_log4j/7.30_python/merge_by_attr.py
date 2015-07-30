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

if __name__ == "__main__":
    ''' run this conmand like this: cat tag_account.cnt.final.deleteDigit.seg | python2.6 merge_by_attr.py'''
    remain_attr = [14,16,22,31,33]
    remain_attr_str = ['14','16','22','31','33']
    del_attr = [15,25,26,30,34,35,36,37]
    del_attr_str = ['15','25','26','30','34','35','36','37']
    list_start = ['一','以','为']
    cnt = 0
    attr = load_attr_list.get_attr_list()
    regex = '\t'
    fp = open('./tag_final','w')
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
            # del
            if int(w_nums[0]) not in remain_attr:
                #cnt += 1
                #print "%s" % (new_line)
                continue
            else:
                fp.write(new_line + "\n")
            '''
            del_fp = open((pre_file_path + w_nums[0]).strip(),'a')
            del_fp.write(new_line + '\n')
            del_fp.close()
            continue
            '''

        else:
            #if (int(words[1]) < 160 and len(set(w_nums) & set(del_attr_str))>=1) or (len(w_nums)>3) or (words[0].find('一')!=-1 or words[0].find('为')!=-1 or words[0].find('以')!=-1):
            if (len(set(w_nums) & set(del_attr_str))>=1) or (len(set(w_nums) & set(remain_attr_str))<1) or (len(w_nums)>3) or (words[0].find('一')!=-1 or words[0].find('为')!=-1 or words[0].find('以')!=-1):
                cnt+=1
                #print "****<60"
                continue
            try:
                flag = 0
                for w_num in w_nums:
                    #if (int(w_num)) in del_attr and len(words[0].strip())==2:
                    if (int(w_num)) in del_attr and len(words[0].strip())==4:
                        cnt += 1
                        print line,'***dd'
                        flag = 1
                        break
                    new_line += (attr[int(w_num)] + ' ')
                if flag:
                    continue
            except:
                print >> sys.stderr, "ERROR in int %s" % (words[3])
            fp.write(new_line.strip() + "\n")
            print "%%%%right"
        '''
        else:
            if int(words[1]) < 20 and len(set(w_nums) & set(del_attr_str))>=2:
                cnt+=1
                print "****<20"
                continue
            if str(34) in w_nums or (len(w_nums)==2 and w_nums[0] in del_attr_str and w_nums[1] in del_attr_str):
            #if str(34) in w_nums:
                cnt += 1
                print line,'***34'
                continue
            try:
                flag = 0
                for w_num in w_nums:
                    #if (int(w_num)) in del_attr and len(words[0].strip())==2:
                    if (int(w_num)) in del_attr and len(words[0].strip())==4:
                        cnt += 1
                        print line,'***dd'
                        flag = 1
                        break
                    new_line += (attr[int(w_num)] + ' ')
                if flag:
                    continue
            except:
                print >> sys.stderr, "ERROR in int %s" % (words[3])
            fp.write(new_line.strip() + "\n")
        '''
    fp.close()
    print >> sys.stderr, "the del lines is %d" % (cnt)
    print "END..."

