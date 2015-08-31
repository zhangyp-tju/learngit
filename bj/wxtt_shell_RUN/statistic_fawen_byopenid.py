#!/usr/bin/python2.6
#coding=utf-8

import sys
import os

url_dic = {}
open_id_dic = {}
DEBUG = 0
alph = 60 # 60 秒
def statistic_by_time(filepath):
    regex='\t'
    cnt = 0
    err_cnt = 0
    with open(filepath,'r') as fp:
        for line in fp:
            cnt += 1
            line = line.strip()
            if not line:
                continue
            cols = line.split(regex)
            if len(cols) != 7:
                #print "Error line: %s" % (line)
                err_cnt += 1
                continue
            eles = cols[-3].split("##")
            if len(eles) < 2:
                open_id = eles[0]
            else:
                open_id = eles[1]
            if open_id not in open_id_dic:
                open_id_dic[open_id] = []
            #open_id_dic[open_id].append(int(cols[-2])) # time  TypeError: sequence item 0: expected string, int found
            open_id_dic[open_id].append(cols[-2]) # time 在后面的使用地方在 int去

            #print cols[5],open_id
        print >> sys.stderr, "Lines Numbers : %d   ERROR LINEs : %d" % (cnt,err_cnt)

def load_file(filename):
    regex='\t'
    cnt = 0
    with open(filename,'r') as fp:
        for line in fp:
            cnt += 1
            line = line.strip()
            if not line:
                continue
            cols = line.split(regex)
            if len(cols) != 7:
                print >> sys.stderr,"Error line: %s" % (line)
                continue
            url_dic[cols[0]] = url_dic.get(cols[0],0) + 1 # cols[0] ---- url
            #print cols[0]
        print >> sys.stderr,"Lines Numbers : %d" % (cnt)


# 处理结果
def statistic_results_group_write(file_path):
    #file_path = "/search/yapeng/check_data/lhb_zyp/out_arts_group"
    with open(file_path,'w') as fw:
        for open_id,time_list in open_id_dic.items():
            # 排序
            time_list.sort()
            group_list = []
            if int(time_list[-1]) - int(time_list[0]) < alph:
                group_list.append('-'.join(time_list))
            else:
                time_list_len = len(time_list)
                start = 0
                for i in range(1,time_list_len):# [1,len)
                    if int(time_list[i]) - int(time_list[i-1]) > alph:
                        group_list.append('-'.join(time_list[start:i])) # [start,i) 是下标
                        start = i
                # 增加最后一组
                group_list.append('-'.join(time_list[start:i]))
            fw.write(open_id + "\t" + str(len(time_list)) + "\t" + '\t'.join(group_list) + "\n")




# 所有的文件进行统计的
def list_dir(dir_path,out_path):
    global DEBUG
    flag = 1
    if not os.path.isdir(dir_path):
        print "ERROR CMD -- not a dir Usage: statistic_fawen_byopenid.py [FOLDER_SRC] [FILE_OUT]"
        exit(1)
    list_name = os.listdir(dir_path)
    for name in list_name:
        current_path = os.path.join(dir_path,name)
        if os.path.isdir(current_path):
            list_dir(current_path)
        elif os.path.isfile(current_path):
            print "file %s" % current_path
            if flag:
                # 按照每一个文件统计结果,每一天的
                statistic_by_time(current_path)
            if DEBUG:
                flag = 0
    # 把统计并排序的按照时间分组的结果保存 --- 独立运行
    statistic_results_group_write(out_path)
    # 清空全局变量 open_id_dic
    open_id_dic.clear()

# need two args: first for dir_src second for file_path ()
def main_statistic_openid_timestamp():
    current_path = os.getcwd()
    print "参数0：%s" % (sys.argv[0])
    if len(sys.argv) < 3:
        print >> sys.stderr,"ERROR CMD(main_statistic_openid_timestamp)...Usage:tatistic_fawen_byopenid.py [FOLDER_SRC] [FILE_OUT]"
        exit(1)
    dir_path = os.path.join(current_path,sys.argv[1])
    out_path = os.path.join(current_path,sys.argv[2])
    list_dir(dir_path,out_path) # this is the main function


if __name__ == "__main__":
    main_statistic_openid_timestamp()
