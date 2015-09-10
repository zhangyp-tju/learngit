#!/usr/bin/python
# -*- encoding: gbk -*-

import time
import sys
from trie import Dict

DIC = Dict("./region_dic")
openid_name_dic = {}

def match_server(string):
    return DIC.match_all(string)

def parse(title,openid_name):
    if openid_name in openid_name_dic:
        # 0--文章总数；
        openid_name_dic[openid_name][0] += 1
        # 1--nameInTitle
        if openid_name_dic[openid_name][1][0] in title: # name
            openid_name_dic[openid_name][1][1] += 1
        # 2--regionInTitleName(a list 0 for area 1 for cnt)
        area = openid_name_dic[openid_name][2][0]
        if area in title:
            openid_name_dic[openid_name][2][1] += 1
        # 3--region only in Title (a dic key is area_name,value is cnt)
        area_t = match_server(title.decode("gbk"))
        if area_t != []:
            for gov in set(area_t):
                gov = gov.encode("gbk")
                openid_name_dic[openid_name][3][gov] = openid_name_dic[openid_name][3].get(gov,0) + 1
    else:
        # 0--文章总数；1--nameInTitle(a list 0 for name 1 for cnt)；2--regionInTitleName(a list 0 for area 1 for cnt) 3--region only in Title (a dic key is area_name,value is cnt)
        openid_name_dic[openid_name] = [0,["None",0],["None",0],{}]
        # 0--文章总数；
        openid_name_dic[openid_name][0] += 1
        # 1--nameInTitle(a list 0 for name 1 for cnt)
        try:
            name = openid_name.split("##")[0]
        except:
            print >> sys.stderr, "ERROR:%d" % (openid_name)
            return
        openid_name_dic[openid_name][1][0] = name
        if name in title:
            openid_name_dic[openid_name][1][1] += 1
        # 2--regionInTitleName(a list 0 for area 1 for cnt)
        area = match_server(name.decode("gbk"))
        if area == []:
            return
        openid_name_dic[openid_name][2][0] = area[0].encode("gbk")
        if openid_name_dic[openid_name][2][0] in title:
            openid_name_dic[openid_name][2][1] += 1
        # 3--region only in Title (a dic key is area_name,value is cnt)
        area_t = match_server(title.decode("gbk"))
        if area_t != []:
            for gov in set(area_t):
                gov = gov.encode("gbk")
                openid_name_dic[openid_name][3][gov] = 1


def filter_area():
    err_cnt = 0
    regex = "\t"
    for line in sys.stdin:
        line = line.strip()
        if not line:
            err_cnt += 1
            continue
        cols = line.split(regex)
        try:
            title = cols[1]
            openid_name = cols[-3]
        except:
            err_cnt += 1
            continue
        parse(title,openid_name)

    print >> sys.stderr, "ERROR:%d" % (err_cnt)

def write_result():
    print "openid_name\t发文总数\tNameInTitle\tAreaInNameInTitle\tAreaIntitle[list]"
    for openid_name, val_list in openid_name_dic.items():
        if val_list[3] == {}:
            print "%s\t%d\t%d\t%d\t0" % (openid_name,val_list[0],val_list[1][1],val_list[2][1])
        else:
            list3 = sorted(val_list[3].items(),key=lambda d:d[1],reverse=True)
            lis3 = []
            for gov,cnt in list3:
                lis3.append(gov)
                lis3.append(str(cnt))
            print "%s\t%d\t%d\t%d\t%s" % (openid_name,val_list[0],val_list[1][1],val_list[2][1],"\t".join(lis3))


def main():
    filter_area()
    write_result()
if __name__ == "__main__":
    main()
